import re
p=lambda g:exec(r"g[:]=zip(*eval(re.sub(r'0(?=.{34}(.{35})*([1-9]).{34}\2.{31}\2)',r'\2',str(g)))[::-1]);"*4)or g