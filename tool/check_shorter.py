from glob import glob
import os
import shutil

def check(master_files, dev_branch_files, dev_branch_name):
    mnames = {os.path.basename(f): f for f in master_files}
    dbnames = {os.path.basename(f): f for f in dev_branch_files}

    extra = set(dbnames) - set(mnames)

    if extra:
        print(f"❌ {dev_branch_name}: {', '.join(sorted(extra))}")

    for name in sorted(set(mnames) & set(dbnames)):
        try:
            with open(mnames[name]) as fm, open(dbnames[name]) as fb:
                mlen = len(fm.read())
                dblen = len(fb.read())
            if mlen > dblen:
                print(f"❌ {name}: master={mlen} bytes, {dev_branch_name}={dblen} bytes (master not shorter)")
            # else:
            #     print(f"✅ {name}: master shorter ({mlen} < {dblen})")
        except UnicodeError:
            print(f"{name}: File may contain BOM")

def main():
    master_branch = "master"
    dev_branches = ["moto", "sktkmozt", "bono"]
    master_files = glob("./code/*.py")

    for dev_branch in dev_branches:
        os.system(f"git checkout {dev_branch} && cp -r ./code ./{dev_branch}")
        os.system(f"git checkout {master_branch}")

        dev_files = glob(f"./{dev_branch}/*.py")
        check(master_files, dev_files, dev_branch)

        shutil.rmtree(f"./{dev_branch}")

if __name__ == "__main__":
    main()
