import bz2
import base64
import gzip
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
        zlib_len = len(base64.b64encode(zlib.compress(our_code.encode(), level=9)).decode())
        gzip_len = len(base64.b64encode(gzip.compress(our_code.encode(), compresslevel=9)).decode())
        bz2_len = len(base64.b64encode(bz2.compress(our_code.encode(), compresslevel=9)).decode())
        actual_zlib_len = zlib_len + 62
        actual_gzip_len = gzip_len + 62
        actual_bz2_len = bz2_len + 60

        print(f"\033[92mour                   : {len(our_code)}\033[0m", end=" ")

        if actual_zlib_len < len(our_code) or actual_gzip_len < len(our_code):
            print("\033[93mDo compress!!\033[0m")
        else:
            print()

        print(f"\033[92mour compressed (zlib) : {actual_zlib_len}\033[0m")
        print(f"\033[92mour compressed (gzip) : {actual_gzip_len}\033[0m")
        print(f"\033[92mour compressed (bz2)  : {actual_bz2_len}\033[0m")

    if pub_code:
        zlib_len = len(base64.b64encode(zlib.compress(pub_code.encode(), level=9)).decode())
        gzip_len = len(base64.b64encode(gzip.compress(pub_code.encode(), compresslevel=9)).decode())
        bz2_len = len(base64.b64encode(bz2.compress(pub_code.encode(), compresslevel=9)).decode())
        actual_zlib_len = zlib_len + 62
        actual_gzip_len = gzip_len + 62
        actual_bz2_len = bz2_len + 60

        print(f"\033[94mpub                   : {len(pub_code)}\033[0m", end=" ")

        if actual_zlib_len < len(pub_code) or actual_gzip_len < len(pub_code) or actual_bz2_len < len(pub_code):
            print("\033[93mDo compress!!\033[0m")
        else:
            print()

        print(f"\033[94mpub compressed (zlib) : {actual_zlib_len}\033[0m")
        print(f"\033[94mpub compressed (gzip) : {actual_gzip_len}\033[0m")
        print(f"\033[94mpub compressed (bz2)  : {actual_bz2_len}\033[0m")

    print("-"*35)