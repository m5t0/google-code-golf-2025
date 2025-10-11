import re
p=lambda g:exec("g[:]=zip(*eval(re.sub(r'3, ([0,\s]*)0, ([1-9])',r'3,\\1\\2,\\2',str(g)))[::-1]);"*28)or g