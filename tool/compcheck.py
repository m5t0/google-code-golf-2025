import os
import sys
from zlib import compress

start = 1
end = 400

if len(sys.argv) == 2:
    end = int(sys.argv[1])

if len(sys.argv) > 2:
    start = int(sys.argv[1])
    end = int(sys.argv[2])

def zip_src(src):
 compression_level = 9 # Max Compression

 # We prefer that compressed source not end in a quotation mark
 while (compressed := compress(src.encode(), compression_level))[-1] == ord('"'): src += b"#"

 def sanitize(b_in):
  """Clean up problematic bytes in compressed b-string"""
  b_out = bytearray()
  for b in b_in:
   if   b==0:         b_out += b"\\x00"
   elif b==ord("\r"): b_out += b"\\r"
   elif b==ord("\\"): b_out += b"\\\\"
   else: b_out.append(b)
  return b"" + b_out

 compressed = sanitize(compressed)

 delim = b'"""' if ord("\n") in compressed or ord('"') in compressed else b'"'

 return b"#coding:L1\nimport zlib\nexec(zlib.decompress(bytes(" + \
  delim + compressed + delim + \
  b',"L1")))'

def process_code(author, code, color, out=None, write=False):
    clear = "\033[0m"
    compressed_code = zip_src(code)
    improvement = len(code) - len(compressed_code)

    print(f"{color}{author}            : {len(code)}{clear}")

    if write:
        assert out

        os.makedirs(os.path.dirname(out), exist_ok=True)

        with open(out, mode='wb') as f:
            f.write(compressed_code if improvement > 0 else code.encode())

    if write and improvement > 0:
        print(f"Wrote to {out} (reduced {improvement} bytes)")

    return improvement if improvement > 0 else 0

total_reduced = 0

for i in range(start, end + 1):
    task = f"task{str(i).zfill(3)}.py"
    our = f"./code/{task}"
    pub = f"./input/solution2/{task}"
    out = f"./submission/{task}"

    print(" " * 10 + "\033[4m" + task + "\033[0m")

    if our_code := open(our, mode='r').read() if os.path.isfile(our) else "":
        total_reduced += process_code("our", our_code, "\033[92m", out, True)
    # if pub_code := open(pub, mode='r').read() if os.path.isfile(pub) else "":
    #     process_code("pub", pub_code, "\033[94m")

    print("-"*35)

print(f"Total Reduced: {total_reduced} bytes")