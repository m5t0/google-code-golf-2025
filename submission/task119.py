import re
p=lambda g:exec('g[:]=eval(re.sub("0(?=.{40}[38].{40}[382])","3",str([*zip(*g)][::-1])));'*40)or g