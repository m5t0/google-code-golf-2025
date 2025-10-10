import re
p=lambda g:exec("g[:]=zip(*eval(re.sub(r'2, 0,([\d,\s]*)3',r'2,3,\\1 0',re.sub(r'1, 0,([\d,\s]*)7',r'1,7,\\1 0',str(g))))[::-1]);"*8)or g