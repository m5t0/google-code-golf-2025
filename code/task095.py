import re
p=lambda g:exec("g[:]=zip(*eval(re.sub(r'0, ([1-9]), 0',r'1,\\1,1',str(g))));"*2)or g