# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module containing utilities for the 2025 Google Code Golf Championship."""

import copy
import contextlib
import importlib.util
import io
import json
import numpy
import os
import re
import sys
import traceback

import matplotlib.pyplot as plt
import numpy as np

code_golf_dir = "./input/google-code-golf-2025/"
libraries = ["collections", "itertools", "math", "operator", "re", "string",
             "struct"]
modes = [NORMAL := "normal", DEBUG := "debug"]
colors = [
    (0, 0, 0),
    (30, 147, 255),
    (250, 61, 49),
    (78, 204, 48),
    (255, 221, 0),
    (153, 153, 153),
    (229, 59, 163),
    (255, 133, 28),
    (136, 216, 241),
    (147, 17, 49),
]
task_zero = {
    "train": [{
        "input": [
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [5, 1, 1, 1, 1, 1, 1, 5, 5, 5],
            [5, 1, 1, 1, 1, 1, 1, 5, 5, 5],
            [5, 1, 1, 1, 1, 1, 1, 5, 5, 5],
            [5, 1, 1, 1, 1, 1, 1, 5, 5, 5],
            [5, 1, 1, 1, 1, 1, 1, 5, 5, 5],
            [5, 1, 1, 1, 1, 1, 1, 5, 5, 5],
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        ],
        "output": [
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [5, 1, 1, 1, 1, 1, 1, 5, 5, 5],
            [5, 1, 1, 1, 1, 1, 1, 0, 5, 5],
            [5, 1, 1, 1, 1, 1, 1, 0, 5, 5],
            [5, 1, 1, 1, 1, 1, 1, 0, 5, 5],
            [5, 1, 1, 1, 1, 1, 1, 0, 5, 5],
            [5, 1, 1, 1, 1, 1, 1, 0, 5, 5],
            [5, 5, 0, 0, 0, 0, 0, 0, 5, 5],
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        ],
    }],
    "test": [{
        "input": [
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [5, 5, 4, 4, 4, 4, 4, 4, 5, 5],
            [5, 5, 4, 4, 4, 4, 4, 4, 5, 5],
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [5, 5, 4, 4, 4, 4, 4, 5, 5, 5],
            [5, 5, 4, 5, 5, 5, 4, 5, 5, 5],
            [5, 5, 4, 5, 5, 5, 4, 5, 5, 5],
            [5, 5, 4, 4, 4, 4, 4, 5, 5, 5],
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        ],
        "output": [
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [5, 5, 4, 4, 4, 4, 4, 4, 5, 5],
            [5, 5, 4, 4, 4, 4, 4, 4, 0, 5],
            [5, 5, 5, 0, 0, 0, 0, 0, 0, 5],
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [5, 5, 4, 4, 4, 4, 4, 5, 5, 5],
            [5, 5, 4, 0, 0, 0, 4, 0, 5, 5],
            [5, 5, 4, 0, 5, 5, 4, 0, 5, 5],
            [5, 5, 4, 4, 4, 4, 4, 0, 5, 5],
            [5, 5, 5, 0, 0, 0, 0, 0, 5, 5],
        ],
    }],
    "arc-gen": [{
        "input": [
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [5, 5, 2, 2, 2, 2, 2, 2, 5, 5],
            [5, 5, 2, 5, 5, 5, 5, 2, 5, 5],
            [5, 5, 2, 5, 5, 5, 5, 2, 5, 5],
            [5, 5, 2, 5, 5, 5, 5, 2, 5, 5],
            [5, 5, 2, 5, 5, 5, 5, 2, 5, 5],
            [5, 5, 2, 2, 2, 2, 2, 2, 5, 5],
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        ],
        "output": [
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [5, 5, 2, 2, 2, 2, 2, 2, 5, 5],
            [5, 5, 2, 0, 0, 0, 0, 2, 0, 5],
            [5, 5, 2, 0, 5, 5, 5, 2, 0, 5],
            [5, 5, 2, 0, 5, 5, 5, 2, 0, 5],
            [5, 5, 2, 0, 5, 5, 5, 2, 0, 5],
            [5, 5, 2, 2, 2, 2, 2, 2, 0, 5],
            [5, 5, 5, 0, 0, 0, 0, 0, 0, 5],
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        ],
    }],
}


def load_examples(task_num):
    """Loads relevant data from ARC-AGI and ARC-GEN."""
    if not task_num:
        return task_zero
    with open(code_golf_dir + f"task{task_num:03d}.json") as f:
        examples = json.load(f)
    return examples


def show_legend():
    image = [[(255, 255, 255) for _ in range(21)] for _ in range(3)]
    for idx, color in enumerate(colors):
        image[1][2 * idx + 1] = color
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.imshow(np.array(image))
    for idx, _ in enumerate(colors):
        color = "white" if idx in [0, 9] else "black"
        ax.text(2 * idx + 0.9, 1.1, str(idx), color=color)
    ax.set_xticks([])
    ax.set_yticks([])


def show_examples(examples, bgcolor=(255, 255, 255)):
    # Determine the dimensions of the image to be rendered.
    width, height, offset = 0, 0, 1
    for example in examples:
        grid, output = example["input"], example["output"]
        width += len(grid[0]) + 1 + len(output[0]) + 4
        height = max(height, max(len(grid), len(output)) + 4)
    # Determine the contents of the image.
    image = [[bgcolor for _ in range(width)] for _ in range(height)]
    for example in examples:
        grid, output = example["input"], example["output"]
        grid_width, output_width = len(grid[0]), len(output[0])
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                image[r + 2][offset + c + 1] = colors[cell]
        offset += grid_width + 1
        for r, row in enumerate(output):
            for c, cell in enumerate(row):
                image[r + 2][offset + c + 1] = colors[cell]
        offset += output_width + 4
    # Draw the image.
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.imshow(np.array(image))
    # Draw the horizontal and vertical lines.
    offset = 1
    for example in examples:
        grid, output = example["input"], example["output"]
        grid_width, grid_height = len(grid[0]), len(grid)
        output_width, output_height = len(output[0]), len(output)
        ax.hlines([r + 1.5 for r in range(grid_height + 1)],
                  xmin=offset + 0.5, xmax=offset + grid_width + 0.5, color="black")
        ax.vlines([offset + c + 0.5 for c in range(grid_width + 1)],
                  ymin=1.5, ymax=grid_height + 1.5, color="black")
        offset += grid_width + 1
        ax.hlines([r + 1.5 for r in range(output_height + 1)],
                  xmin=offset + 0.5, xmax=offset + output_width + 0.5, color="black")
        ax.vlines([offset + c + 0.5 for c in range(output_width + 1)],
                  ymin=1.5, ymax=output_height + 1.5, color="black")
        offset += output_width + 2
        ax.vlines([offset + 0.5], ymin=-0.5, ymax=height - 0.5, color="black")
        offset += 2
    ax.set_xticks([])
    ax.set_yticks([])


def verify_program(task_num, examples, task_path="/kaggle/working/task.py", mode=NORMAL):
    task_name = "task_with_imports"
    spec = importlib.util.spec_from_file_location(task_name, task_path)
    if spec is None:
        print("Error: Unable to import task.py.")
        return
    module = sys.modules[task_name] = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not hasattr(module, "p"):
        print("Error: Unable to locate function p() in task.py.")
        return
    program = getattr(module, "p")
    if not callable(program):
        print("Error: Function p() in task.py is not callable.")
        return
    print()

    def colorize(arr):
        def rgb_bg(r, g, b):
            return f"\033[48;2;{r};{g};{b}m"

        clear = "\033[0m"

        s = str(arr)

        for i in range(1, 10):
            bg = rgb_bg(*((180, 180, 210) if i == 5 else colors[i]))

            while f" {i} " in s or f"[{i} " in s or f" {i}]" in s or f"[{i}]" in s:
                s = s.replace(f" {i} ", f" {bg}{i}{clear} ").replace(f"[{i} ", f"[{bg}{i}{clear} ").replace(f" {i}]",
                                                                                                            f" {bg}{i}{clear}]").replace(
                    f"[{i}]",
                    f"[{bg}{i}{clear}]")
        return s

    def verify(example_subset):
        right, wrong, error = 0, 0, ''

        def debug_output(res):
            nonlocal buf, right, wrong, error

            user_output = None
            converted = True

            try:
                user_output = np.array(res)
            except:
                converted = False

            example_input = np.array(example_copy["input"])
            label_output = np.array(example_copy["output"])

            is_right = res is not None and converted and numpy.array_equal(user_output, label_output)

            if is_right:
                right += 1
            if not is_right or mode == DEBUG:
                if res is not None and not (is_right and mode == DEBUG):
                    wrong += 1

                colorized_input, colorized_label, colorized_output = colorize(
                    example_input), colorize(label_output), colorize(user_output)

                if converted:
                    margin = 4

                    print("Input".center(len(str(example_input).split('\n')[0])))
                    print(colorized_input)

                    raw_label_lines = str(label_output).split('\n')
                    raw_user_lines = str(user_output).split('\n')

                    label_lines = colorized_label.split('\n')
                    user_lines = colorized_output.split('\n')

                    max_lines = max(len(raw_label_lines), len(raw_user_lines))
                    max_width = max(max(len(rl) for rl in raw_label_lines), len("Correct Output"))

                    raw_label_lines += [''] * (max_lines - len(raw_label_lines))
                    raw_user_lines += [''] * (max_lines - len(raw_user_lines))

                    label_lines += [''] * (max_lines - len(label_lines))
                    user_lines += [''] * (max_lines - len(user_lines))

                    header1 = "Correct Output".center(len(raw_label_lines[0]))
                    header2 = ' ' * (max_width + margin - len(header1)) + "Your Output".center(
                        len(raw_user_lines[0]))
                    print(header1 + header2)

                    for (rl, l, ru, u) in zip(raw_label_lines, label_lines, raw_user_lines, user_lines):
                        print(l + ' ' * (max_width + margin - len(rl)) + u)
                else:
                    from pprint import pprint

                    print("Input")
                    print(colorized_input)
                    print("Correct Output")
                    print(colorized_label)
                    print("Your Output")
                    pprint(res)

            if (not is_right or mode == DEBUG) and (captured := buf.getvalue().strip()):
                print("Your Debug Output")
                print(captured)

            if error:                         print(f"\nError: {error.strip()}")
            if not is_right or mode == DEBUG: print('-' * 45)

        for example in example_subset:
            error = ""
            example_copy = copy.deepcopy(example)
            try:
                buf = io.StringIO()
                with contextlib.redirect_stdout(buf):
                    result = program(copy.deepcopy(example_copy["input"]))
                result = json.dumps(result)
                result = result.replace("true", "1").replace("false", "0")
                unsafe_chars = re.compile(r"[^0-9,\[\]\s\.]")
                if unsafe_chars.search(result):
                    raise ValueError(f"Invalid output from user code: {result[:500]}")
                result = json.loads(result)
                debug_output(result)
            except:
                error = traceback.format_exc()
                wrong += 1
                debug_output(None)

        return right, wrong

    arc_agi_right, arc_agi_wrong = verify(examples["train"] + examples["test"])
    arc_gen_right, arc_gen_wrong = verify(examples["arc-gen"])
    print(f"Results on ARC-AGI examples: {arc_agi_right} pass, {arc_agi_wrong} fail")
    print(f"Results on ARC-GEN examples: {arc_gen_right} pass, {arc_gen_wrong} fail")
    print()
    if arc_agi_wrong + arc_gen_wrong == 0:
        task_length = os.path.getsize(task_path)
        print("Your code IS READY for submission!")
        print("Its length appears to be " + str(task_length) + " bytes.")
        print("Next steps:")
        print(" * Copy it into a file named task{:03d}.py on your local machine.".format(task_num))
        print(" * Create a zip file containing that program along with all others.")
        print(" * Submit that zip file to the Kaggle competition so that it can be officially scored.")
    else:
        print("Your code IS NOT ready for submission.")