import re
p=lambda g:exec('g[:]=eval(re.sub("0(?=.{40}[13-9].{40}[1-9])","3",str([*zip(*g)][::-1])));'*40)or g