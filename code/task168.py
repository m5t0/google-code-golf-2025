import re
p=lambda g:exec(r"g[:]=zip(*eval(re.sub(r'0(?=.{37}(?:.{35})*([1-9]).{28}\1, \1)',r'\1',str(g)))[::-1]);"*4)or g