import re
p=lambda g:exec(r"g[:]=zip(*eval(re.sub(r'0(?=.{34}(?:.{35})*([^0]).{34}\1.{31}\1, \1)',r'\1',str(g)))[::-1]);"*4)or g