import re
p=lambda g:exec('g[:]=eval(re.sub("0(?=(?!.{40}2).{40}[^0].{40}[1-9])","3",str([*zip(*g)][::-1])));'*40)or g