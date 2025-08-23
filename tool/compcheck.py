import base64
import os
import sys
import zlib

start = 1
end = 100

if len(sys.argv) == 2:
    end = int(sys.argv[1])

if len(sys.argv) > 2:
    start = int(sys.argv[1])
    end = int(sys.argv[2])

for i in range(start, end + 1):
    task = f"task{str(i).zfill(3)}.py"
    our = f"./code/{task}"
    pub = f"./input/solution2/{task}"

    our_code = open(our, mode='r').read() if os.path.isfile(our) else ""
    pub_code = open(pub, mode='r').read() if os.path.isfile(pub) else ""

    print(" " * 10 + "\033[4m" + task + "\033[0m")

    if our_code:
        compressed_len = len(base64.b64encode(zlib.compress(our_code.encode())).decode())
        actual_compressed_len = compressed_len + 62

        print(f"\033[92mour            : {len(our_code)}\033[0m")
        print(f"\033[92mour compressed : {actual_compressed_len}\033[0m",end=" ")

        if actual_compressed_len < len(our_code):
            print("\033[93mDo compress!!\033[0m")
        else:
            print()

    if pub_code:
        compressed_len = len(base64.b64encode(zlib.compress(pub_code.encode())).decode())
        actual_compressed_len = compressed_len + 62

        print(f"\033[94mpub            : {len(pub_code)}\033[0m")
        print(f"\033[94mpub compressed : {actual_compressed_len}\033[0m", end=" ")

        if actual_compressed_len < len(pub_code):
            print("\033[93mDo compress!!\033[0m")
        else:
            print()

    print("-"*35)