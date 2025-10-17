import re
p=lambda g:exec('g[:]=zip(*eval(re.sub("0(?=.{40}[38].{40}[382])","3",str(g)))[::-1]);'*40)or g