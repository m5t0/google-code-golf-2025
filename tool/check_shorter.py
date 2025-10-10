from glob import glob
import os
import shutil
import subprocess


def run_cmd(cmd):
    subprocess.run(cmd, shell=True, check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def check(master_files, dev_branch_files, dev_branch_name):
    ok = True

    mnames = {os.path.basename(f): f for f in master_files}
    dbnames = {os.path.basename(f): f for f in dev_branch_files}

    extra = set(dbnames) - set(mnames)

    if extra:
        print(f"❌ {dev_branch_name}: {', '.join(sorted(extra))}")
        ok = False

    for name in sorted(set(mnames) & set(dbnames)):
        if os.path.isfile(
                mreplaced := os.path.join(os.path.dirname(mnames[name]), "../submission", name)) and os.path.isfile(
                dbreplaced := os.path.join(os.path.dirname(dbnames[name]), "../submission", name)):
            mnames[name] = mreplaced
            dbnames[name] = dbreplaced

        try:
            with open(mnames[name]) as fm, open(dbnames[name]) as fb:
                mlen = len(fm.read())
                dblen = len(fb.read())
            if mlen > dblen:
                print(f"❌ {name}: master={mlen} bytes, {dev_branch_name}={dblen} bytes (master not shorter)")
                ok = False
            # else:
            #     print(f"✅ {name}: master shorter ({mlen} < {dblen})")
        except UnicodeError:
            if "submission" not in mnames[name] + dbnames[name]:
                print(f"{name}: File may contain BOM")

    if ok:
        print(f"✅ {dev_branch_name}: OK")


def main():
    master_branch = "master"
    dev_branches = ["moto", "sktkmozt", "bono", "Lucien"]

    run_cmd("git checkout master && git pull")
    master_files = glob("./code/*.py")

    for dev_branch in dev_branches:
        try:
            run_cmd(f"git checkout {dev_branch} && git pull")

            shutil.copytree("./code", f"./{dev_branch}/code", dirs_exist_ok=True)

            if os.path.isdir("./submission"):
                shutil.copytree("./submission", f"./{dev_branch}/submission", dirs_exist_ok=True)

            run_cmd(f"git checkout {master_branch}")

            dev_files = glob(f"./{dev_branch}/code/*.py")
            check(master_files, dev_files, dev_branch)
        finally:
            if os.path.isdir(f"./{dev_branch}"):
                shutil.rmtree(f"./{dev_branch}")


if __name__ == "__main__":
    main()
