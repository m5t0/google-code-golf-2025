import ast, keyword, re, random, json, zopfli.zlib, copy, sys, os, zipfile, glob, warnings, zlib, time
import threading, ctypes
from queue import Queue
sys.path.append("./input/google-code-golf-2025/code_golf_utils")
from code_golf_utils import *

UNSAFE_MODE = False
SCORE_TIMEOUT_TIME = 1 # seconds
VALIDATE_TIMEOUT_TIME = 60 # seconds

def create_template_from_function(code_string: str) -> (str, list):
    tree = ast.parse(code_string)
    variable_names = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name) and node.id not in keyword.kwlist and node.id not in ['Counter', 'next', 'int', 'chain','enumerate', 'combinations', 'product', 'str', 'abs', 'exec', 'eval', 'len', 'min', 'max', 'range', 'set','any', 'filter', 'list', 'map', 'sum', 'tuple', 'zip', 'all', 'sorted']}
    template = code_string
    for name in sorted(list(variable_names), key=len, reverse=True):
        template = re.sub(r'\b' + re.escape(name) + r'\b', f'##{name}##', template)
    return template.replace("def ##p##", "def p").replace("##p##=lambda", "p=lambda").replace("##f##'", "f'").replace('##f##"', 'f"'), sorted(list(variable_names))

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
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def raise_exception(self):
        thread_id = self.get_id()
        resu = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), ctypes.py_object(SystemExit))
        if resu > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), 0)

def run_with_thread_timeout(func, timeout, *args, **kwargs):
    """
    Execute a function in a separate thread with a timeout.
    """
    result_queue = Queue()
    x = CustomThread(name = 'Thread', target=func, args=(*args,result_queue), kwargs=kwargs)
    x.start()
    x.join(timeout)
    alive = x.is_alive()
    if alive:
        x.raise_exception()
    x.join()
    assert not x.is_alive()

    if alive:
        raise Exception()
    try:
        return result_queue.get()
    except Exception:
        raise

def get_score_runner(code: str, examples_to_check: list, result_queue: Queue) -> (int, int):
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=SyntaxWarning)
            solution_namespace = {}
            exec(code, solution_namespace)
            p_func = solution_namespace.get('p')
            for _, example in examples_to_check:
                if json.dumps(p_func(copy.deepcopy(example['input']))) != json.dumps(example['output']):
                    result_queue.put((999,999))
                    return
            compressed = zopfli.zlib.compress(code.encode())
            # compressed = zlib.compress(code.encode(), 9)
            penalty = sum(compressed.count(c) for c in [b'\\', b'\0', b'\n', b'\r']) + min(compressed.count(b"'"), compressed.count(b'"'))
            result_queue.put((len(compressed), penalty))
            return
    except Exception:
        result_queue.put((998, 998))
        return

def get_score(code: str, examples_to_check: list) -> (int, int):
    try:
        return run_with_thread_timeout(get_score_runner,SCORE_TIMEOUT_TIME,code,examples_to_check)
    except Exception:
        return 1000, 1000

def validate_code_runner(code: str, all_examples_to_check: list, result_queue: Queue) -> tuple | None:
    """Checks code against all examples. Returns the first failing example or None."""
    if UNSAFE_MODE: all_examples_to_check = all_examples_to_check[:1]
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=SyntaxWarning)
            # signal.alarm(1)
            solution_namespace = {}
            exec(code, solution_namespace)
            p_func = solution_namespace.get('p')
            # signal.alarm(0)
            
            for i, example in all_examples_to_check:
                # signal.alarm(1)
                if json.dumps(p_func(copy.deepcopy(example['input']))) != json.dumps(example['output']):
                    # signal.alarm(0)
                    result_queue.put((i,example))
                    return # FAILED
                # signal.alarm(0)
            result_queue.put(None)
            return # PASSED
    except Exception:
        # Code fails to execute, so it's invalid. Return the first example as the failure point.
        result_queue.put(all_examples_to_check[0])
        return

def validate_code(code: str, all_examples_to_check: list) -> tuple | None:
    """Checks code against all examples. Returns the first failing example or None."""
    try:
        return run_with_thread_timeout(validate_code_runner,VALIDATE_TIMEOUT_TIME,code,all_examples_to_check)
    except Exception:
        # Code fails to execute, so it's invalid. Return the first example as the failure point.
        return all_examples_to_check[0]

if __name__ == '__main__':
    TASK_ID = int(sys.argv[1])
    filename = f"./code/task{TASK_ID:03d}.py"

    print('*'*60)
    print(filename, TASK_ID)

    # --- Setup ---
    with open(filename,"r") as h:
     RAW_FUNCTION_STRING = h.read().strip()

    task_data = load_examples(TASK_ID)
    all_examples = list(enumerate(task_data.get('train', []) + task_data.get('test', []) + task_data.get('arc-gen', [])))
    checked_examples = [ex for ex in all_examples if ex[0] in [240]]
    checked_example_ids = {ex[0] for ex in checked_examples}

    # --- Optimization Pipeline ---
    FUNCTION_TEMPLATE, original_vars = create_template_from_function(RAW_FUNCTION_STRING)
    print(f"Initial variables: {original_vars}\n")
    candidate_names = list("qertyuiopasdfghjklzxcbnm")

    initial_code = FUNCTION_TEMPLATE.replace("##", "")
    PAYLOAD_OVERHEAD = 60

    # --- Initial Validation ---
    print("Running initial validation against all examples...")
    if validate_code(initial_code, all_examples) is not None:
        print("FATAL: Initial raw function is incorrect. Exiting.")
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

    print(f"Initial size: {global_best_total_size} (Base: {current_base}, Penalty: {current_penalty})\n{initial_code}\n" + "-" * 30)

    LIMIT = 6000
    REBASE_INTERVAL = 500
    NEXT_REBASE = 500

    for i in range(LIMIT):
        if i > 0 and i % NEXT_REBASE == 0:
            REBASE_INTERVAL *= 1.3
            NEXT_REBASE += REBASE_INTERVAL
            print(f"\n--- Rebase at iter {i}: Validating global best (Size: {global_best_total_size}) ---")

            failing_example = validate_code(global_best_code, all_examples)

            if failing_example:
                fail_id, fail_ex = failing_example
                print(f"VALIDATION FAILED on example #{fail_id}! Reverting to last known good solution.")
                # Revert global best to the last one that passed
                global_best_code = last_known_good_code
                global_best_base, global_best_penalty = last_known_good_base, last_known_good_penalty
                global_best_total_size = last_known_good_total_size
                print(f"Reverted to size: {global_best_total_size}")

                # Add the new failing example to the checked set if it's not already there
                if fail_id not in checked_example_ids:
                    checked_example_ids.add(fail_id)
                    checked_examples = [ex for ex in all_examples if ex[0] in checked_example_ids]
                    print(f"Added example #{fail_id} to the active test set. (Now checking {len(checked_examples)} examples)")
            else:
                # Update the checkpoint to the current global best
                last_known_good_code = global_best_code
                last_known_good_base, last_known_good_penalty = global_best_base, global_best_penalty
                last_known_good_total_size = global_best_total_size

            FUNCTION_TEMPLATE, original_vars = create_template_from_function(global_best_code)
            current_mapping = {var: var for var in original_vars}
            current_base, current_penalty = get_score(global_best_code, checked_examples) # Rescore with potentially new examples
            print(f"New rebase variables: {original_vars}\n" + "-" * 30)

        if not original_vars: continue
        trial_mapping = {var: var for var in original_vars} # Start from identity map for the current template
        num_changes = random.randint(1, min(6, len(original_vars)))
        vars_to_change = random.sample(original_vars, k=num_changes)
        for var, new_name in zip(vars_to_change, random.sample(candidate_names, k=num_changes)):
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
                print(f"\nNew best: {trial_total_size} (B:{global_best_base}, P:{global_best_penalty}) @{i+1}")
                print(trial_code)
            global_best_total_size = trial_total_size

    # --- Final Result ---
    print(f"\nFinal validation of best code found...")
    if validate_code(global_best_code, all_examples) is not None:
        print("WARNING: The final best code failed full validation. Something may be wrong.")
    else:
        print("Final code PASSED validation.")

    print(f"\nBest score achieved: {global_best_total_size} bytes (Base: {global_best_base}, Penalty: {global_best_penalty})")
    print("\nFinal optimized code:")
    with open(filename, "w") as h:
     h.write(global_best_code)
