import code_golf_utils
import os
import sys

task_num = 2
task_dir = "./code/"

if len(sys.argv) == 1:
    sys.argv.append(str(task_num))

if ".." not in sys.argv[-1] and not sys.argv[-1].isdigit():
    task_dir = sys.argv[-1]
    sys.argv.pop()

for i in range(1, len(sys.argv))[::-1]:
    if ".." in sys.argv[i]:
        start, end = sys.argv[i].split("..")
        sys.argv.pop(i)

        for j in range(int(start), int(end) + 1):
            sys.argv.append(str(j))

for arg in sys.argv[1:]:
    task_num = int(arg)
    task_path = f"{task_dir}/task{str(task_num).zfill(3)}.py"

    if os.path.isfile(task_path):
        examples = code_golf_utils.load_examples(task_num=task_num)
        code_golf_utils.verify_program(
            task_num=task_num, examples=examples, task_path=task_path
        )
