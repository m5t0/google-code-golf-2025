import code_golf_utils
import sys

task_num = 5

if len(sys.argv) > 1:
    task_num = int(sys.argv[1])

task_path = f"./code/task{str(task_num).zfill(3)}.py"
examples = code_golf_utils.load_examples(task_num=task_num)
code_golf_utils.verify_program(
    task_num=task_num, examples=examples, task_path=task_path
)
