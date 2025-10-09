import re
p=lambda g:exec("g[:]=zip(*eval(re.sub(r'8([0,\s]{3,})([1-9])',r'\\2\\1\\2',str(g)))[::-1]);"*4)or g