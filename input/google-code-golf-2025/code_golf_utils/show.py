import code_golf_utils
import matplotlib.pyplot as plt
import sys

task_num = 2
task_name = "arc-gen"  # train, test, arc-gen
s = 0
num = 5

if len(sys.argv) > 1:
    task_num = int(sys.argv[1])

examples = code_golf_utils.load_examples(task_num=task_num)[task_name][s:s+num]
code_golf_utils.show_examples(examples=examples)
# code_golf_utils.show_legend()
plt.show()

# 色
# 0:黒、1:青、2:赤、3:緑、4:黄土、5:灰、6:ピンク紫、7:橙、8:水、9:茶
