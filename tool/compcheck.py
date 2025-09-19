import copy
import importlib.util
import os
import sys
import concurrent.futures
from threading import Lock

MAX_WORKERS = 32

DEFLATE = 0
ZOPFLI = 1
ZLIB = 2

for i in range(1, len(sys.argv))[::-1]:
    if ".." in sys.argv[i]:
        start, end = sys.argv[i].split("..")
        sys.argv.pop(i)

        for j in range(int(start), int(end) + 1):
            sys.argv.append(str(j))

def zip_src(task_num, src, baseline, compressor=DEFLATE):
    margin = 10

    def compress_custom(data, level):
        if compressor == DEFLATE:
            import deflate
            return deflate.deflate_compress(data, compresslevel=level)
        elif compressor == ZOPFLI:
            import zopfli.zopfli
            return zopfli.zopfli.compress(data, numiterations=128, blocksplitting=False)[2:-4]
        elif compressor == ZLIB:
            import zlib
            comp = zlib.compressobj(level=level, memLevel=9, wbits=-9)
            compressed = comp.compress(data) + comp.flush()
            return compressed
        else:
            print("Unknown compressor")
            return b""

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

    def is_valid(compressed, delim_start, delim_end, check_result=False, check_all=False):
        def check(path):
            spec = importlib.util.spec_from_file_location("code_golf_utils",
                                                          "./input/google-code-golf-2025/code_golf_utils/code_golf_utils.py")
            code_golf_utils = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(code_golf_utils)
            task_data = code_golf_utils.load_examples(task_num)

            try:
                task_name = "task_with_imports"
                spec = importlib.util.spec_from_file_location(task_name, path)

                if spec is None:
                    return False

                module = sys.modules[task_name] = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                if not hasattr(module, "p"):
                    return False

                if not callable(program := getattr(module, 'p')):
                    return False

                if not check_result:
                    return True

                all_examples = task_data["train"] + task_data["test"] + task_data["arc-gen"]

                if not check_all:
                    all_examples = all_examples[:1]

                for example in all_examples:
                    input_grid = copy.deepcopy(example["input"])
                    expected = example["output"]
                    try:
                        actual = program(input_grid)
                        if actual != expected:
                            return False
                    except:
                        return False
                return True
            except:
                return False

        src = get_src(compressed, delim_start, delim_end)

        try:
            import tempfile

            with tempfile.NamedTemporaryFile(suffix=".py", mode="wb", delete=False) as f:
                f.write(src)

            res = check(f.name)
            os.remove(f.name)
            return res
        except:
            return False

    best = None

    for level in range(1, 13 if compressor == DEFLATE else 2 if compressor == ZOPFLI else 10):
        # We prefer that compressed source not end in a quotation mark
        while (compressed := compress_custom(src.encode(), level=level))[-1] == ord('"'): src += "#"

        for delim_start, delim_end in [(b'"', b'"'), (b"'", b"'"), (b'r"', b'"'), (b"r'", b"'"), (b'"""', b'"""')]:
            if is_valid(compressed, delim_start, delim_end):
                break

        if not is_valid(compressed, delim_start, delim_end, check_result=True):
            compressed = sanitize(compressed)

        while True:
            current_len = len(compressed)

            for i in range(len(compressed)):
                if compressed[i] == 120:
                    trimmed = compressed[:i] + compressed[i + 1:]

                    if is_valid(trimmed, delim_start, delim_end, check_result=True):
                        compressed = trimmed
                        break

            if len(compressed) == current_len:
                break

        if not is_valid(compressed, delim_start, delim_end, check_result=True):
            continue

        s = get_src(compressed, delim_start, delim_end)

        if best is None or len(s) < len(best):
            best = s

        if len(best) > baseline + margin:
            break

    return b' ' * 10000 if best is None else best


class Counter:
    def __init__(self):
        self.deflate_cnt = 0
        self.zopfli_cnt = 0
        self.zlib_cnt = 0
        self.total_saved = 0
        self.lock = Lock()

    def update(self, improvement, compressor):
        with self.lock:
            self.total_saved += improvement
            if compressor == DEFLATE:
                self.deflate_cnt += 1
            elif compressor == ZOPFLI:
                self.zopfli_cnt += 1
            elif compressor == ZLIB:
                self.zlib_cnt += 1


def process_task(task_num, counter):
    task = f"task{str(task_num).zfill(3)}.py"
    our = f"./code/{task}"
    pub = f"./input/solution2/{task}"
    out = f"./submission/{task}"

    output_lines = []
    output_lines.append(" " * 10 + "\033[4m" + task + "\033[0m")

    if os.path.isfile(our):
        our_code = open(our, mode='r').read()
        improvement, compressor_used, output_str = process_code_single(task_num, "our", our_code, "\033[92m", out, True)
        output_lines.append(output_str)
        if improvement > 0:
            output_lines.append(f"Wrote to {out} (saved {improvement} bytes)")
        counter.update(improvement, compressor_used)
    else:
        output_lines.append("our code not found")

    output_lines.append("-" * 35)
    return "\n".join(output_lines)


def process_code_single(task_num, author, code, color, out=None, write=False):
    clear = "\033[0m"
    deflate = zip_src(task_num, code, len(code), compressor=DEFLATE)
    zopfli = zip_src(task_num, code, len(code), compressor=ZOPFLI)
    zlib = zip_src(task_num, code, len(code), compressor=ZLIB)
    compressed_code = min(deflate, zopfli, zlib, key=len)

    if deflate == compressed_code:
        compressor_used = DEFLATE
    elif zopfli == compressed_code:
        compressor_used = ZOPFLI
    elif zlib == compressed_code:
        compressor_used = ZLIB
    else:
        compressor_used = -1

    improvement = len(code) - len(compressed_code)
    if improvement < 0:
        improvement = 0

    output_str = f"{color}{author}            : {len(code)}{clear}"

    if write and improvement > 0:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, mode='wb') as f:
            f.write(compressed_code)

    return improvement, compressor_used, output_str


def main():
    if len(sys.argv) < 2:
        return

    counter = Counter()
    tasks = [int(arg) for arg in sys.argv[1:]]

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(process_task, task_num, counter) for task_num in tasks]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

    print(f"Total saved: {counter.total_saved} bytes")
    print(f"Deflate: {counter.deflate_cnt} times")
    print(f"Zopfli: {counter.zopfli_cnt} times")
    print(f"Zlib: {counter.zlib_cnt} times")


if __name__ == "__main__":
    main()