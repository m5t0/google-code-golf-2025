import re
p=lambda g:exec("g[:]=zip(*eval(re.sub(r'0, .(?=, 0|\\))','0,0',str(g)))[::-1]);"*8)or g