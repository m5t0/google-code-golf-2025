import ast, keyword, re, random, json, copy, sys, os, zipfile, glob, warnings, zlib, time
import threading, ctypes
from queue import Queue
import numpy as np
import pickle
import argparse

sys.path.append("./input/google-code-golf-2025/code_golf_utils")
from code_golf_utils import *
from typing import Callable, Any

UNSAFE_MODE = False
SCORE_TIMEOUT_TIME = 1  # seconds
VALIDATE_TIMEOUT_TIME = 60  # seconds
FINAL_VALIDATE_TIMEOUT_TIME = 300  # seconds
COMPRESSOR = "zopfli"


# ---------------- load compcheck cache ------------------------
def load_compressor_from_cache(task_id: int, default: str) -> str:
    try:
        with open("./tool/cache.pkl", "rb") as f:
            data = pickle.load(f)
            compressor = ["deflate", "zopfli", "zlib"][data[task_id][0]]
            print(f"Loaded compressor type {compressor} from the cache")
            return compressor
    except Exception as e:
        print(f"WARNING:Raised exception while reading the cache")
        return default


# ------------------ multithread utility ------------------------------


# referenced:https://qiita.com/76r6qo698/items/5fdad284ebc547baf324
class CustomThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
        threading.Thread.__init__(self, group=group, target=target, name=name)
        self.args = args
        self.kwargs = kwargs
        return

    def run(self):
        self._target(*self.args, **self.kwargs)

    def get_id(self):
        if hasattr(self, "_thread_id"):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def raise_exception(self):
        thread_id = self.get_id()
        resu = ctypes.pythonapi.PyThreadState_SetAsyncExc(
            ctypes.c_long(thread_id), ctypes.py_object(SystemExit)
        )
        if resu > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), 0)


def run_with_thread_timeout(
    func: Callable[..., Any], timeout: int | float, *args: Any, **kwargs: Any
) -> Any:
    """
    Execute a function in a separate thread with a timeout.
    """
    result_queue = Queue()
    x = CustomThread(
        name="Thread", target=func, args=(*args, result_queue), kwargs=kwargs
    )
    x.start()
    x.join(timeout)
    alive = x.is_alive()
    if alive:
        x.raise_exception()
    x.join()
    assert not x.is_alive()

    if alive:
        raise TimeoutError()
    try:
        return result_queue.get()
    except Exception:
        raise


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


def validate_code_runner(
    code: str, examples_to_check: list, unsafe_mode: bool, result_queue: Queue
) -> None:
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
                    result_queue.put((i, example))
                    return  # FAILED
            result_queue.put(None)
            return  # PASSED
    except Exception:
        # Code fails to execute, so it's invalid. Return the first example as the failure point.
        result_queue.put(examples_to_check[0])
        return


def validate_code(
    code: str,
    examples_to_check: list,
    timeout: int | float = VALIDATE_TIMEOUT_TIME,
    unsafe_mode=UNSAFE_MODE,
) -> tuple[int, list] | None:
    """Checks code against all examples. Returns the first failing example or None."""
    try:
        return run_with_thread_timeout(
            validate_code_runner, timeout, code, examples_to_check, unsafe_mode
        )
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
    compressor: str = COMPRESSOR,
    timeout: int | float = SCORE_TIMEOUT_TIME,
) -> tuple[int, int]:
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=SyntaxWarning)
            failing_example = validate_code(code, examples_to_check, timeout=timeout)
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


def main():
    global \
        UNSAFE_MODE, \
        SCORE_TIMEOUT_TIME, \
        VALIDATE_TIMEOUT_TIME, \
        FINAL_VALIDATE_TIMEOUT_TIME, \
        COMPRESSOR

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
        "--limit", type=int, default=6000, help="limit of the number of trials"
    )
    parser.add_argument(
        "--rebase-interval",
        type=int,
        default=500,
        help="a parameter that determines the speed of the meter's increase until the next rebase",
    )
    parser.add_argument(
        "--next-rebase",
        type=int,
        default=500,
        help="a parameter that determines the size of meter until the next rebase",
    )
    parser.add_argument(
        "--rebase-interval-scaling",
        type=float,
        default=1.3,
        help="a parameter that controls the degree of increase (scaling) of the rebase_interval",
    )
    parser.add_argument(
        "--unsafe",
        default=UNSAFE_MODE,
        action="store_true",
        help="validate only with 1 example when this option exists",
    )
    parser.add_argument(
        "--use-compcheck-cache",
        default=True,
        help="use compcheck cache to determine the compressor type",
    )

    args = parser.parse_args()

    TASK_ID = args.task_id
    filename = f"./code/task{TASK_ID:03d}.py"
    COMPRESSOR = args.compressor
    SCORE_TIMEOUT_TIME = args.score_timeout
    VALIDATE_TIMEOUT_TIME = args.validate_timeout
    FINAL_VALIDATE_TIMEOUT_TIME = args.final_validate_timeout
    LIMIT = args.limit
    REBASE_INTERVAL = args.rebase_interval
    NEXT_REBASE = args.next_rebase
    REBASE_INTERVAL_SCALING = args.rebase_interval_scaling
    UNSAFE_MODE = args.unsafe

    if args.use_compcheck_cache:
        COMPRESSOR = load_compressor_from_cache(TASK_ID, COMPRESSOR)

    print("*" * 60)
    print(filename, TASK_ID)

    # --- Setup ---
    with open(filename, "r") as h:
        RAW_FUNCTION_STRING = h.read().strip()

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
    print(f"Initial variables: {original_vars}\n")
    candidate_names = list("qertyuiopasdfghjklzxcbnm")

    initial_code = FUNCTION_TEMPLATE.replace("##", "")
    PAYLOAD_OVERHEAD = 63

    # --- Initial Validation ---
    print("Running initial validation against all examples...")
    if validate_code(initial_code, all_examples) is not None:
        print(
            "task{TASK_ID:03d} FATAL: Initial raw function is incorrect. Exiting.",
            file=sys.stderr,
        )
        raise ValueError("Failed with original")
    print("Initial code PASSED validation.")

    current_base, current_penalty = get_score(initial_code, checked_examples)
    current_total_size = PAYLOAD_OVERHEAD + current_base + current_penalty

    # Global best tracking
    global_best_code = initial_code
    global_best_base, global_best_penalty = current_base, current_penalty
    global_best_total_size = current_total_size

    # Last known good tracking
    last_known_good_code = initial_code
    last_known_good_base, last_known_good_penalty = current_base, current_penalty
    last_known_good_total_size = current_total_size

    print(
        f"Initial size: {global_best_total_size} (Base: {current_base}, Penalty: {current_penalty})\n{initial_code}\n"
        + "-" * 30
    )

    if (
        PAYLOAD_OVERHEAD + global_best_base + global_best_penalty
        > len(initial_code) + 20
    ):
        print("Compressed code is too longer than uncompressed code, so quit.")
        print(
            f"Uncompressed Code:{len(initial_code)} bytes, Compressed Code:{PAYLOAD_OVERHEAD + global_best_base + global_best_penalty} bytes"
        )
        return

    for i in range(LIMIT):
        if i > 0 and i % NEXT_REBASE == 0:
            REBASE_INTERVAL *= REBASE_INTERVAL_SCALING
            NEXT_REBASE += REBASE_INTERVAL
            print(
                f"\n--- Rebase at iter {i}: Validating global best (Size: {global_best_total_size}) ---"
            )

            failing_example = validate_code(global_best_code, all_examples)

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

            FUNCTION_TEMPLATE, original_vars = create_template_from_function(
                global_best_code
            )
            current_base, current_penalty = get_score(
                global_best_code, checked_examples
            )  # Rescore with potentially new examples
            print(f"New rebase variables: {original_vars}\n" + "-" * 30)

        if not original_vars:
            continue
        trial_mapping = {
            var: var for var in original_vars
        }  # Start from identity map for the current template
        num_changes = random.randint(1, min(6, len(original_vars)))
        vars_to_change = random.sample(original_vars, k=num_changes)
        for var, new_name in zip(
            vars_to_change, random.sample(candidate_names, k=num_changes)
        ):
            trial_mapping[var] = new_name

        trial_code = FUNCTION_TEMPLATE
        for var in original_vars:
            trial_code = trial_code.replace(f"##{var}##", trial_mapping[var])

        trial_base, trial_penalty = get_score(trial_code, checked_examples)
        trial_total_size = PAYLOAD_OVERHEAD + trial_base + trial_penalty

        if trial_total_size <= global_best_total_size:
            global_best_code = trial_code
            global_best_base, global_best_penalty = trial_base, trial_penalty
            if trial_total_size < global_best_total_size:
                print(
                    f"\nNew best: {trial_total_size} (B:{global_best_base}, P:{global_best_penalty}) @{i + 1}"
                )
                print(trial_code)
            global_best_total_size = trial_total_size

    # --- Final Result ---
    print(f"\nFinal validation of best code found...")
    if (
        validate_code(
            global_best_code,
            all_examples,
            timeout=FINAL_VALIDATE_TIMEOUT_TIME,
            unsafe_mode=False,
        )
        is not None
    ):
        print(
            f"task{TASK_ID:03d} WARNING: The final best code failed full validation. Something may be wrong.(This warning sometimes occur due to the unsafe option.)",
            file=sys.stderr,
        )
        return
    else:
        print("Final code PASSED validation.")

    print(
        f"\nBest score achieved: {global_best_total_size} bytes (Base: {global_best_base}, Penalty: {global_best_penalty})"
    )
    print("\nFinal optimized code:")
    print(global_best_code)

    if PAYLOAD_OVERHEAD + sum(get_score(global_best_code, checked_examples)) < min(
        len(initial_code),
        PAYLOAD_OVERHEAD + sum(get_score(initial_code, checked_examples)),
    ):
        print("Write the best code to the file!")
        with open(filename, "w") as h:
            h.write(global_best_code)
    else:
        print(
            "Don't write the best code to the file because it's not shorter than the initial code."
        )


if __name__ == "__main__":
    main()
