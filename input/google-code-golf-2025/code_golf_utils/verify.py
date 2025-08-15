import code_golf_utils

task_num = 4
task_path = "./code/task4.py"
examples = code_golf_utils.load_examples(task_num=task_num)
code_golf_utils.verify_program(
    task_num=task_num, examples=examples, task_path=task_path
)
