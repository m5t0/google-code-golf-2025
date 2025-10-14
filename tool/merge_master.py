from glob import glob
import os
import shutil
import subprocess


def run_cmd(cmd):
    subprocess.run(cmd, shell=True, check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    run_cmd("git checkout master && git pull")
    shutil.copytree("./code", f"./master/code", dirs_exist_ok=True)
    shutil.copytree("./submission", f"./master/submission", dirs_exist_ok=True)
    run_cmd("git checkout kaz")

    for task_num in range(1, 400):
        task_file = f"task{task_num:03d}.py"

        if os.path.getsize(f"./master/submission/{task_file}") < os.path.getsize(f"./submission/{task_file}"):
            shutil.copyfile(f"./master/code/{task_file}", f"./code/{task_file}")
            shutil.copyfile(f"./master/submission/{task_file}", f"./submission/{task_file}")

    shutil.rmtree("./master")


if __name__ == "__main__":
    main()
