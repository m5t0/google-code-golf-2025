import copy
import importlib.util
import os
import sys
import zlib

start = 1
end = 400

if len(sys.argv) == 2:
    end = int(sys.argv[1])

if len(sys.argv) > 2:
    start = int(sys.argv[1])
    end = int(sys.argv[2])

def zip_src(task_num, src):
    def compress_custom(data, level, wbits):
        comp = zlib.compressobj(level=level, memLevel=9, wbits=wbits)
        compressed = comp.compress(data) + comp.flush()
        return compressed

    get_src = lambda c, ds, de: b"#coding:L1\nimport zlib\nexec(zlib.decompress(bytes(" + ds + c + de + b',"L1"),-9))'

    def sanitize(b_in):
        """Clean up problematic bytes in compressed b-string"""
        b_out = bytearray()
        for b in b_in:
            if b == 0:
                b_out += b"\\x00"
            elif b == ord("\r"):
                b_out += b"\\r"
            elif b == ord("\\"):
                b_out += b"\\\\"
            else:
                b_out.append(b)
        return b"" + b_out

    def is_valid(compressed, delim_start, delim_end, check_result=False):
        def check(solution):
            spec = importlib.util.spec_from_file_location("code_golf_utils", "./input/google-code-golf-2025/code_golf_utils/code_golf_utils.py")
            code_golf_utils = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(code_golf_utils)
            task_data = code_golf_utils.load_examples(task_num)

            try:
                namespace = {}
                exec(solution, namespace)
                if 'p' not in namespace: return False
                all_examples = task_data['train'] + task_data['test'] + task_data['arc-gen']
                for example in all_examples:
                    input_grid = copy.deepcopy(example['input'])
                    expected = example['output']
                    try:
                        actual = namespace['p'](input_grid)
                        if actual != expected:
                            return False
                    except:
                        return False
                return True
            except Exception as e:
                return False

        src = get_src(compressed, delim_start, delim_end)

        try:
            if check_result:
                return check(src.decode("L1"))
            exec(src.decode("L1"))
            return True
        except Exception:
            return False

    best = None

    for i in range(1, 10):
        # We prefer that compressed source not end in a quotation mark
        while (compressed := compress_custom(src.encode(), level=i, wbits=-9))[-1] == ord('"'): src += b"#"

        for delim_start, delim_end in [(b'"', b'"'), (b"'", b"'"), (b'r"', b'"'), (b"r'", b"'"), (b'"""', b'"""')]:
            if is_valid(compressed, delim_start, delim_end):
                break

        if not is_valid(compressed, delim_start, delim_end):
            compressed = sanitize(compressed)

        while True:
            current_len = len(compressed)

            for i in range(len(compressed)):
                if compressed[i] == 120:
                    trimmed = compressed[:i] + compressed[i+1:]

                    if is_valid(trimmed, delim_start, delim_end, check_result=True):
                        compressed = trimmed
                        break

            if len(compressed) == current_len:
                break

        s = get_src(compressed, delim_start, delim_end)

        if best is None or len(s) < len(best):
            best = s

    return best

def process_code(task_num, author, code, color, out=None, write=False):
    clear = "\033[0m"
    compressed_code = zip_src(task_num, code)
    improvement = len(code) - len(compressed_code)

    print(f"{color}{author}            : {len(code)}{clear}")

    if write:
        assert out

        os.makedirs(os.path.dirname(out), exist_ok=True)

        with open(out, mode='wb') as f:
            f.write(compressed_code if improvement > 0 else code.encode())

    if write and improvement > 0:
        print(f"Wrote to {out} (saved {improvement} bytes)")

    return improvement if improvement > 0 else 0

total_saved = 0

for i in range(start, end + 1):
    task = f"task{str(i).zfill(3)}.py"
    our = f"./code/{task}"
    pub = f"./input/solution2/{task}"
    out = f"./submission/{task}"

    print(" " * 10 + "\033[4m" + task + "\033[0m")

    if our_code := open(our, mode='r').read() if os.path.isfile(our) else "":
        total_saved += process_code(i, "our", our_code, "\033[92m", out, True)
    # if pub_code := open(pub, mode='r').read() if os.path.isfile(pub) else "":
    #     process_code("pub", pub_code, "\033[94m")

    print("-"*35)

print(f"Total saved: {total_saved} bytes")