import re
s=re.sub
p=lambda g:exec(r"g[:]=zip(*eval(s('2, 0,([\d, ]*)3',r'2,3,\1 0',s('1, 0,([\d, ]*)7',r'1,7,\1 0',str(g))))[::-1]);"*8)or g