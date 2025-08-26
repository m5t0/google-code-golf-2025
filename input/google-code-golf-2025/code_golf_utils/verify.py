import code_golf_utils
import sys

task_num = 2
task_dir = "./code/"

if len(sys.argv) == 1:
    sys.argv.append(str(task_num))

if not sys.argv[-1].isdigit():
    task_dir = sys.argv[-1]
    sys.argv.pop()

for i in range(1, len(sys.argv)):
    task_num = int(sys.argv[i])
    task_path = f"{task_dir}/task{str(task_num).zfill(3)}.py"

    examples = code_golf_utils.load_examples(task_num=task_num)
    code_golf_utils.verify_program(
        task_num=task_num, examples=examples, task_path=task_path
    )
