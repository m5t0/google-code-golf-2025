import re
p=lambda g:exec('g[:]=eval(re.sub("0(?=.{40}[^0].{40}[1-9])(?!.{40}2.{40}2)","3",str([*zip(*g)][::-1])));'*40)or g