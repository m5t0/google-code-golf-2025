import ast, keyword, re, random, json, copy, sys, os, zipfile, glob, warnings, zlib, time
import ctypes, concurrent.futures, multiprocessing
import compcheck
import numpy as np
import pickle
import argparse
import time
import math
import psutil

sys.path.append("./input/google-code-golf-2025/code_golf_utils")
from code_golf_utils import *
from typing import Callable, Any


# ---------------- Timer Utility ----------------------------
class Timer:
    def __init__(self):
        self.start()

    def start(self):
        self.start_time = time.time()

    def elapsed_time(self):
        now = time.time()
        s = now - self.start_time
        return s

    def remain_time(self, percent: float):
        s = self.elapsed_time()
        es = s / (percent)
        rs = es - s

        return rs


# ---------------- load compcheck cache ------------------------
def load_compressor_from_cache(task_id: int, default: str) -> str:
    try:
        with open("./tool/cache.pkl", "rb") as f:
            data = pickle.load(f)
            compressor = ["deflate", "zopfli", "zlib"][data[task_id][0]]
            print(f"Loaded compressor type {compressor} from the cache")
            return compressor
    except Exception:
        print(
            f"task{task_id:03d} WARNING:Raised exception while reading the cache",
            file=sys.stderr,
        )
        return default


# ------------------ multithread utility ------------------------------


# Define as top-level function (to make it pickleable)
def _wrapped_func(func, *args, **kwargs):
    """Wrapper function to record process ID"""
    current_process = multiprocessing.current_process()
    pid = current_process.pid

    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(f"Process {pid} encountered an error: {e}")
        raise


class TimeoutProcessPool:
    def __init__(self, max_workers=None):
        self.max_workers = max_workers
        self.executor = concurrent.futures.ProcessPoolExecutor(max_workers=max_workers)
        self._shutdown = False
        self._timeout_occurred = False

    def execute_with_timeout(self, func, timeout, *args, **kwargs):
        if self._shutdown:
            raise RuntimeError("Pool is shutdown")

        # Reinitialize executor if it became unstable from previous timeout
        if self._timeout_occurred:
            self._restart_executor()

        # Use top-level function
        future = self.executor.submit(_wrapped_func, func, *args, **kwargs)
        try:
            result = future.result(timeout=timeout)
            return result
        except concurrent.futures.TimeoutError:
            # Force terminate process on timeout
            # print(
            #     f"Timeout detected for function {func.__name__}, terminating process..."
            # )
            self._terminate_process_tree(future)

            # Set timeout flag and reinitialize executor
            self._timeout_occurred = True
            self._restart_executor()

            raise TimeoutError(
                f"Function {func.__name__} timed out after {timeout} seconds"
            )
        except Exception as e:
            # Check executor status for other exceptions too
            if "broken" in str(e).lower() or "terminated" in str(e).lower():
                self._timeout_occurred = True
                self._restart_executor()
            raise

    def _terminate_process_tree(self, future):
        """Terminate the process tree"""
        try:
            # Identify the running process
            if hasattr(future, "_process") and future._process is not None:
                pid = future._process.pid

                try:
                    # Get the main process
                    parent = psutil.Process(pid)

                    # Terminate the process tree including all child processes
                    children = parent.children(recursive=True)

                    # First terminate child processes
                    for child in children:
                        try:
                            child.terminate()
                        except psutil.NoSuchProcess:
                            pass

                    # Wait for child processes to terminate
                    gone, alive = psutil.wait_procs(children, timeout=5)

                    # Force kill any remaining processes
                    for child in alive:
                        try:
                            child.kill()
                        except psutil.NoSuchProcess:
                            pass

                    # Terminate the parent process
                    try:
                        parent.terminate()
                        parent.wait(timeout=5)
                    except (psutil.NoSuchProcess, psutil.TimeoutExpired):
                        try:
                            parent.kill()
                        except psutil.NoSuchProcess:
                            pass

                except psutil.NoSuchProcess:
                    print(f"Process {pid} no longer exists")
                except Exception as e:
                    print(f"Error terminating process {pid}: {e}")

            # Cancel the Future as well
            future.cancel()

        except Exception as e:
            print(f"Error in process termination: {e}")

    def _restart_executor(self):
        """Reinitialize the executor"""

        # Shutdown the old executor
        try:
            self.executor.shutdown(wait=False)
        except Exception as e:
            print(f"Error during executor shutdown: {e}")

        # Clean up orphaned processes
        self._cleanup_orphaned_processes()

        # Create a new executor
        self.executor = concurrent.futures.ProcessPoolExecutor(
            max_workers=self.max_workers
        )
        self._timeout_occurred = False

    def _cleanup_orphaned_processes(self):
        """Clean up orphaned processes"""
        try:
            current_pid = os.getpid()
            for proc in psutil.process_iter(["pid", "name", "status"]):
                try:
                    # Target Python processes that are not in zombie state
                    if (
                        "python" in proc.info["name"].lower()
                        and proc.info["status"] != psutil.STATUS_ZOMBIE
                        and proc.info["pid"] != current_pid
                    ):
                        # If parent process doesn't exist or parent process is not current process
                        parent = proc.parent()
                        if (
                            parent is None
                            or parent.pid == 1
                            or parent.pid == current_pid
                        ):
                            proc.terminate()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
        except Exception as e:
            print(f"Error during orphaned process cleanup: {e}")

    def shutdown(self, wait=True):
        self._shutdown = True
        self.executor.shutdown(wait=wait)

        # Also clean up residual processes during shutdown
        if not wait:
            self._cleanup_orphaned_processes()


def run_with_thread_timeout(
    func: Callable[..., Any],
    timeout: int | float,
    pool: TimeoutProcessPool,
    *args: Any,
    **kwargs: Any,
) -> Any:
    """
    Execute a function in a separate thread with a timeout.
    """
    return pool.execute_with_timeout(func, timeout, *args, **kwargs)


# ----------------- optimization code -----------------------


def create_template_from_function(code_string: str) -> tuple[str, list]:
    tree = ast.parse(code_string)
    variable_names = {
        node.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Name)
        and node.id not in keyword.kwlist
        and node.id
        not in [
            "Counter",
            "next",
            "int",
            "chain",
            "enumerate",
            "combinations",
            "product",
            "str",
            "abs",
            "exec",
            "eval",
            "len",
            "min",
            "max",
            "range",
            "set",
            "any",
            "filter",
            "list",
            "map",
            "sum",
            "tuple",
            "zip",
            "all",
            "sorted",
        ]
    }
    template = code_string
    for name in sorted(list(variable_names), key=len, reverse=True):
        template = re.sub(r"\b" + re.escape(name) + r"\b", f"##{name}##", template)
    return template.replace("def ##p##", "def p").replace(
        "##p##=lambda", "p=lambda"
    ).replace("##f##'", "f'").replace('##f##"', 'f"'), sorted(list(variable_names))


def verify(output: list, label: list) -> bool:
    if (
        (type(output) is not list and type(output) is not tuple)
        or any(type(v) is not list and type(v) is not tuple for v in output)
        or any(
            type(w) is not int and type(w) is not float and type(w) is not bool
            for v in output
            for w in v
        )
    ):
        return False
    result = json.dumps(output)
    result = result.replace("true", "1").replace("false", "0")
    result = json.loads(result)

    user_output = None
    converted = True

    try:
        user_output = np.array(result)
    except:
        converted = False

    return (
        result is not None
        and converted
        and np.array_equal(user_output, np.array(label))
    )


def validate_code_runner(code: str, examples_to_check: list, unsafe_mode: bool) -> None:
    """Checks code against all examples. Returns the first failing example or None."""
    if unsafe_mode:
        examples_to_check = examples_to_check[:1]
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=SyntaxWarning)
            solution_namespace = {}
            exec(code, solution_namespace)
            p_func = solution_namespace.get("p")

            for i, example in examples_to_check:
                if not verify(
                    p_func(copy.deepcopy(example["input"])), example["output"]
                ):
                    return i, example  # FAILED
            return  # PASSED
    except Exception:
        # Code fails to execute, so it's invalid. Return the first example as the failure point.
        return examples_to_check[0]


def validate_code(
    code: str,
    examples_to_check: list,
    timeout: int | float,
    unsafe_mode: bool,
    phase: str,
    task_id: int,
    pool: TimeoutProcessPool,
) -> tuple[int, list] | None:
    """Checks code against all examples. Returns the first failing example or None."""
    try:
        return run_with_thread_timeout(
            validate_code_runner,
            timeout,
            pool,
            code,
            examples_to_check,
            unsafe_mode,
        )
    except TimeoutError:
        if phase != "scoring":
            print(
                f"task{task_id:03d} WARNING: Raised Timeout Error when {phase}",
                file=sys.stderr,
            )
        return examples_to_check[0]
    except Exception:
        # Code fails to execute, so it's invalid. Return the first example as the failure point.
        return examples_to_check[0]


def compress_custom(compressor: str, data: str):
    if compressor == "deflate":
        import deflate

        return deflate.deflate_compress(data, compresslevel=9)
    elif compressor == "zopfli":
        import zopfli.zopfli

        return zopfli.zopfli.compress(data, numiterations=128, blocksplitting=False)[
            2:-4
        ]
    elif compressor == "zlib":
        import zlib

        comp = zlib.compressobj(level=9, memLevel=9, wbits=-9)
        compressed = comp.compress(data) + comp.flush()
        return compressed
    else:
        raise Exception("Unknown compressor")


def get_score(
    code: str,
    examples_to_check: list,
    compressor: str,
    timeout: int | float,
    task_id: int,
    pool: TimeoutProcessPool,
) -> tuple[int, int]:
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=SyntaxWarning)
            failing_example = validate_code(
                code,
                examples_to_check,
                timeout=timeout,
                unsafe_mode=False,
                phase="scoring",
                task_id=task_id,
                pool=pool,
            )
            if failing_example is not None:
                return 999, 999

            compressed = compress_custom(compressor, code.encode())

            # min(compressed.count(b"'"), compressed.count(b'"')) when use " or ' as delim
            # 4                                                   when use """ or ''' as delim
            penalty = sum(
                compressed.count(c) for c in [b"\\", b"\0", b"\n", b"\r"]
            ) + min(min(compressed.count(b"'"), compressed.count(b'"')), 4)
            return len(compressed), penalty
    except Exception:
        return 998, 998


def change_vars(
    candidate_names: list[str],
    new_vars: list[str],
    num_changes: int,
) -> tuple[str, list[str]]:
    """change several characters"""

    assert 1 <= num_changes <= len(new_vars)

    idx_to_change = random.sample(range(len(new_vars)), k=num_changes)
    for idx in idx_to_change:
        (new_vars[idx],) = random.sample(
            list(set(candidate_names) - {new_vars[idx]}), k=1
        )

    return new_vars


def swap_vars(new_vars: list[str], num_changes: int) -> tuple[str, list[str]]:
    """swap variables"""

    assert 2 <= num_changes <= len(new_vars)

    if num_changes == 2:
        a, b = random.sample(range(len(new_vars)), k=2)
        new_vars[a], new_vars[b] = new_vars[b], new_vars[a]
    elif num_changes == 3:
        a, b, c = random.sample(range(len(new_vars)), k=3)
        new_vars[a], new_vars[b], new_vars[c] = new_vars[b], new_vars[c], new_vars[a]
    else:
        idx_to_change = random.sample(range(len(new_vars)), k=num_changes)
        while True:
            idx_to_change2 = copy.deepcopy(idx_to_change)
            random.shuffle(idx_to_change2)
            if all(idx != idx2 for idx, idx2 in zip(idx_to_change, idx_to_change2)):
                break

        vars = [new_vars[idx] for idx in idx_to_change]
        for idx2, val in zip(idx_to_change2, vars):
            new_vars[idx2] = val

    return new_vars


def main(pool: TimeoutProcessPool):
    TASK_ID = 1
    UNSAFE_MODE = False
    SCORE_TIMEOUT_TIME = 1  # seconds
    VALIDATE_TIMEOUT_TIME = 60  # seconds
    FINAL_VALIDATE_TIMEOUT_TIME = 300  # seconds
    COMPRESSOR = "zopfli"

    parser = argparse.ArgumentParser()
    parser.add_argument("task_id", type=int, help="task id")
    parser.add_argument(
        "--compressor",
        type=str,
        default=COMPRESSOR,
        choices=["zlib", "deflate", "zopfli"],
        help="compressor type",
    )
    parser.add_argument(
        "--score-timeout",
        type=float,
        default=SCORE_TIMEOUT_TIME,
        help="timeout time(seconds) when scoring (only few examples are used when scoring)",
    )
    parser.add_argument(
        "--validate-timeout",
        type=float,
        default=VALIDATE_TIMEOUT_TIME,
        help="timeout time(seconds) when validating (all examples are used when validating)",
    )
    parser.add_argument(
        "--final-validate-timeout",
        type=float,
        default=FINAL_VALIDATE_TIMEOUT_TIME,
        help="timeout time(seconds) when final validating (all examples are used when validating)",
    )
    parser.add_argument(
        "--limit", type=int, default=12000, help="limit of the number of trials"
    )
    parser.add_argument(
        "--kick-interval",
        type=int,
        default=1000,
        help="a parameter that determines the steps until the next kick",
    )
    parser.add_argument(
        "--kick-interval-scaling",
        type=float,
        default=1.0,
        help="a parameter that controls the degree of increase (scaling) of the kick_interval",
    )
    parser.add_argument(
        "--unsafe",
        default=UNSAFE_MODE,
        action="store_true",
        help="validate only with 1 example when this option exists",
    )
    parser.add_argument(
        "--use-compcheck-cache",
        type=bool,
        default=True,
        help="use compcheck cache to determine the compressor type",
    )
    parser.add_argument(
        "--auto-timeout-setting",
        type=bool,
        default=True,
        help="set a timeout by the first execution time",
    )

    args = parser.parse_args()

    TASK_ID = args.task_id
    filename = f"./code/task{TASK_ID:03d}.py"
    COMPRESSOR = args.compressor
    SCORE_TIMEOUT_TIME = args.score_timeout
    VALIDATE_TIMEOUT_TIME = args.validate_timeout
    FINAL_VALIDATE_TIMEOUT_TIME = args.final_validate_timeout
    LIMIT = args.limit
    KICK_INTERVAL = args.kick_interval
    NEXT_KICK = KICK_INTERVAL
    KICK_INTERVAL_SCALING = args.kick_interval_scaling
    NEXT_KICK_LIMIT_START = 0
    UNSAFE_MODE = args.unsafe

    if args.use_compcheck_cache:
        COMPRESSOR = load_compressor_from_cache(TASK_ID, COMPRESSOR)

    warnings.filterwarnings("ignore", category=SyntaxWarning)

    print("*" * 60)
    print(filename, TASK_ID)

    # --- Setup ---
    try:
        with open(filename, "r") as h:
            RAW_FUNCTION_STRING = h.read().strip()
    except Exception:
        print(f"task{TASK_ID:03d} FATAL: Failed to load the file", file=sys.stderr)
        return

    task_data = load_examples(TASK_ID)
    all_examples = list(
        enumerate(
            task_data.get("train", [])
            + task_data.get("test", [])
            + task_data.get("arc-gen", [])
        )
    )
    checked_examples = [ex for ex in all_examples if ex[0] in [240]]
    checked_example_ids = {ex[0] for ex in checked_examples}

    # --- Optimization Pipeline ---
    FUNCTION_TEMPLATE, original_vars = create_template_from_function(
        RAW_FUNCTION_STRING
    )
    new_vars = copy.deepcopy(original_vars)
    print(f"Initial variables: {original_vars}\n")
    candidate_names = list("abcdefghijklmnopqrstuvwxyz_")

    initial_code = FUNCTION_TEMPLATE.replace("##", "")
    PAYLOAD_OVERHEAD = 63

    # --- Initial Validation ---
    print("Running initial validation against all examples...")
    timer = Timer()
    if (
        validate_code(
            initial_code,
            all_examples,
            timeout=None,
            unsafe_mode=False,
            phase="validating",
            task_id=TASK_ID,
            pool=pool,
        )
        is not None
    ):
        print(
            f"task{TASK_ID:03d} FATAL: Initial code didn't pass the test. Exiting.",
            file=sys.stderr,
        )
        return

    print("Initial code PASSED validation.")

    running_time = timer.elapsed_time()
    if args.auto_timeout_setting:
        SCORE_TIMEOUT_TIME = max(1, running_time / 10)
        VALIDATE_TIMEOUT_TIME = (
            running_time * 2 if not UNSAFE_MODE else max(1, running_time / 10)
        )
        FINAL_VALIDATE_TIMEOUT_TIME = running_time * 10

        print(
            f"Setting timeout automatically. score_timeout:{SCORE_TIMEOUT_TIME:.2f}s, validate_timeout:{VALIDATE_TIMEOUT_TIME:.2f}s, final_vaildate_timeout:{FINAL_VALIDATE_TIMEOUT_TIME:.2f}s"
        )

    current_base, current_penalty = get_score(
        initial_code,
        checked_examples,
        compressor=COMPRESSOR,
        timeout=SCORE_TIMEOUT_TIME,
        task_id=TASK_ID,
        pool=pool,
    )
    current_total_size = PAYLOAD_OVERHEAD + current_base + current_penalty

    # Global best tracking
    global_best_code = initial_code
    global_best_base, global_best_penalty = current_base, current_penalty
    global_best_total_size = current_total_size

    compcheck_timer = Timer()

    print(f"compcheck consumed time: {compcheck_timer.elapsed_time():.3f}s")

    # Last known good tracking
    last_known_good_code = initial_code
    last_known_good_base, last_known_good_penalty = current_base, current_penalty
    last_known_good_total_size = current_total_size

    if (
        PAYLOAD_OVERHEAD + global_best_base + global_best_penalty
        > len(initial_code) + 30
    ):
        print("Compressed code is too longer than uncompressed code, so quit.")
        print(
            f"Uncompressed Code:{len(initial_code)} bytes, Compressed Code:{PAYLOAD_OVERHEAD + global_best_base + global_best_penalty} bytes"
        )
        print(
            "task{0:03d}: {1} bytes".format(
                TASK_ID,
                min(
                    len(initial_code),
                    PAYLOAD_OVERHEAD
                    + sum(
                        get_score(
                            initial_code,
                            checked_examples,
                            compressor=COMPRESSOR,
                            timeout=SCORE_TIMEOUT_TIME,
                            task_id=TASK_ID,
                            pool=pool,
                        )
                    ),
                ),
            ),
            file=sys.stderr,
        )
        return

    print(
        f"Initial score {global_best_total_size} (Base: {current_base}, Penalty: {current_penalty})\n{initial_code}\n\n"
    )
    print(
        f"initial variables: {new_vars}, size:{PAYLOAD_OVERHEAD + current_base + current_penalty}\n"
        + "-" * 30
    )

    for i in range(LIMIT):
        if i > 0 and i % NEXT_KICK == 0:
            KICK_INTERVAL *= KICK_INTERVAL_SCALING
            NEXT_KICK += KICK_INTERVAL
            NEXT_KICK_LIMIT_START = NEXT_KICK
            print(
                f"\n--- Checkpoint at iter {i}: Validating global best (Size: {global_best_total_size}) ---"
            )

            failing_example = validate_code(
                global_best_code,
                all_examples,
                timeout=VALIDATE_TIMEOUT_TIME,
                unsafe_mode=UNSAFE_MODE,
                phase="validating",
                task_id=TASK_ID,
                pool=pool,
            )

            if failing_example:
                fail_id, fail_ex = failing_example
                print(
                    f"VALIDATION FAILED on example #{fail_id}! Reverting to last known good solution."
                )
                # Revert global best to the last one that passed
                global_best_code = last_known_good_code
                global_best_base, global_best_penalty = (
                    last_known_good_base,
                    last_known_good_penalty,
                )
                global_best_total_size = last_known_good_total_size
                print(f"Reverted to size: {global_best_total_size}")

                # Add the new failing example to the checked set if it's not already there
                if fail_id not in checked_example_ids:
                    checked_example_ids.add(fail_id)
                    checked_examples = [
                        ex for ex in all_examples if ex[0] in checked_example_ids
                    ]
                    print(
                        f"Added example #{fail_id} to the active test set. (Now checking {len(checked_examples)} examples)"
                    )
            else:
                # Update the checkpoint to the current global best
                last_known_good_code = global_best_code
                last_known_good_base, last_known_good_penalty = (
                    global_best_base,
                    global_best_penalty,
                )
                last_known_good_total_size = global_best_total_size

            # ---------------- kick ------------------------
            while True:
                random_value = random.random()
                new_vars2 = copy.deepcopy(new_vars)
                if len(new_vars2) >= 2 and random_value < 0.4:
                    num_changes = random.randint(
                        max(2, len(new_vars2) // 5), max(2, len(new_vars2) * 2 // 5)
                    )
                    new_vars2 = swap_vars(
                        new_vars2,
                        num_changes=num_changes,
                    )
                else:
                    num_changes = random.randint(
                        max(1, len(new_vars2) // 5), max(1, len(new_vars2) * 2 // 5)
                    )
                    new_vars2 = change_vars(
                        candidate_names, new_vars2, num_changes=num_changes
                    )

                trial_code = FUNCTION_TEMPLATE
                for var, var2 in zip(original_vars, new_vars2):
                    trial_code = trial_code.replace(f"##{var}##", var2)

                current_base, current_penalty = get_score(
                    trial_code,
                    checked_examples,
                    compressor=COMPRESSOR,
                    timeout=SCORE_TIMEOUT_TIME,
                    task_id=TASK_ID,
                    pool=pool,
                )

                if PAYLOAD_OVERHEAD + current_base + current_penalty < 1000:
                    new_vars = new_vars2
                    break

            print(
                f"new variables: {new_vars}, size: {PAYLOAD_OVERHEAD + current_base + current_penalty} @{i + 1}"
            )

        # ------------------ neighborhood ------------------------------
        random_value = random.random()
        new_vars2 = copy.deepcopy(new_vars)
        new_vars2 = swap_vars(new_vars2, num_changes=4)
        if len(new_vars2) >= 2 and random_value < 0.3:
            new_vars2 = swap_vars(
                new_vars2,
                num_changes=2,
            )
        elif len(new_vars2) >= 2 and random_value < 0.6:
            new_vars2 = swap_vars(
                new_vars2,
                num_changes=min(3, len(new_vars2)),
            )
        elif random_value < 0.8:
            new_vars2 = change_vars(candidate_names, new_vars2, num_changes=1)
        elif random_value < 0.9:
            new_vars2 = change_vars(
                candidate_names, new_vars2, num_changes=min(2, len(new_vars2))
            )
        else:
            new_vars2 = change_vars(
                candidate_names, new_vars2, num_changes=min(3, len(new_vars2))
            )

        trial_code = FUNCTION_TEMPLATE
        for var, var2 in zip(original_vars, new_vars2):
            trial_code = trial_code.replace(f"##{var}##", var2)

        trial_base, trial_penalty = get_score(
            trial_code,
            checked_examples,
            compressor=COMPRESSOR,
            timeout=SCORE_TIMEOUT_TIME,
            task_id=TASK_ID,
            pool=pool,
        )
        trial_total_size = PAYLOAD_OVERHEAD + trial_base + trial_penalty

        if trial_total_size <= PAYLOAD_OVERHEAD + current_base + current_penalty:
            NEXT_KICK = min(
                NEXT_KICK_LIMIT_START + KICK_INTERVAL * 2,
                NEXT_KICK + KICK_INTERVAL // 10,
            )

            if trial_total_size < PAYLOAD_OVERHEAD + current_base + current_penalty:
                # reset NEXT_KICK_LIMIT_START
                NEXT_KICK_LIMIT_START = max(
                    NEXT_KICK_LIMIT_START, i + KICK_INTERVAL // 2
                )
                NEXT_KICK = max(NEXT_KICK, i + KICK_INTERVAL // 2)

            if (
                trial_total_size
                < PAYLOAD_OVERHEAD + global_best_base + global_best_penalty
            ):
                # reset NEXT_KICK_LIMIT_START
                NEXT_KICK_LIMIT_START = max(
                    NEXT_KICK_LIMIT_START, i + KICK_INTERVAL
                )
                NEXT_KICK = max(NEXT_KICK, i + KICK_INTERVAL)

            new_vars = new_vars2
            current_base = trial_base
            current_penalty = trial_penalty
            print(
                f"new variables: {new_vars2}, size:{PAYLOAD_OVERHEAD + current_base + current_penalty} @{i + 1}"
            )

        if trial_total_size < PAYLOAD_OVERHEAD + global_best_base + global_best_penalty:
            global_best_code = trial_code
            global_best_base, global_best_penalty = trial_base, trial_penalty
            global_best_total_size = trial_total_size
            print(f"\nNew best size: {trial_total_size} @{i + 1}")
            print(trial_code)
            print(f"variables: {new_vars2}, size:{trial_total_size} @{i + 1}")

    # --- Final Result ---
    print(f"\nFinal validation of best code found...")
    if (
        validate_code(
            global_best_code,
            all_examples,
            timeout=FINAL_VALIDATE_TIMEOUT_TIME,
            unsafe_mode=False,
            phase="final validating",
            task_id=TASK_ID,
            pool=pool,
        )
        is not None
    ):
        if (
            validate_code(
                last_known_good_code,
                all_examples,
                timeout=FINAL_VALIDATE_TIMEOUT_TIME,
                unsafe_mode=False,
                phase="validating",
                task_id=TASK_ID,
                pool=pool,
            )
            is not None
        ):
            print(
                f"task{TASK_ID:03d} WARNING: The final best code failed full validation. Something may be wrong.(This warning sometimes occurs when using the unsafe option.)",
                file=sys.stderr,
            )
            return
        else:
            global_best_code = last_known_good_code
            (
                global_best_base,
                global_best_penalty,
            ) = (last_known_good_base, last_known_good_penalty)
            global_best_total_size = last_known_good_total_size

    print("Final code PASSED validation.")

    print(
        f"\nBest score achieved: {global_best_total_size} bytes (Base: {global_best_base}, Penalty: {global_best_penalty})"
    )
    print("\nFinal optimized code:")
    print(global_best_code, end="\n\n")

    # overwrite initial code if submission file exists is shorter than the initial code
    def get_better_submission_code(initial_code):
        submission_file = f"./submission/task{TASK_ID:03d}.py"
        if os.path.exists(submission_file) and os.path.isfile(submission_file):
            try:
                with open(submission_file, "rb") as f:
                    data = f.read()
                    if len(data) < len(initial_code):
                        return data
            except Exception:
                pass

    better_submission_code = get_better_submission_code(initial_code)
    initial_code = (
        better_submission_code if better_submission_code is not None else initial_code
    )

    print(
        f"before best:{len(initial_code)} bytes, varopt compress best:{PAYLOAD_OVERHEAD + global_best_base + global_best_penalty} bytes"
    )

    if PAYLOAD_OVERHEAD + global_best_base + global_best_penalty < len(initial_code):
        print("Write the best code to the file!")
        print(
            "task{0:03d}: {1} bytes -> {2} bytes".format(
                TASK_ID,
                len(initial_code),
                PAYLOAD_OVERHEAD + global_best_base + global_best_penalty,
            ),
            file=sys.stderr,
        )
        with open(filename, "w") as h:
            h.write(global_best_code)
    else:
        print(
            "Don't write the best code to the file because it's not shorter than the initial code."
        )
        print(
            "task{0:03d}: {1} bytes".format(
                TASK_ID,
                len(initial_code),
            ),
            file=sys.stderr,
        )


if __name__ == "__main__":
    pool = TimeoutProcessPool(1)
    try:
        main(pool=pool)
    finally:
        pool.shutdown()
