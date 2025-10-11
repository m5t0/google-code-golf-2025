import re
p=lambda g:exec("g[:]=zip(*eval(re.sub('0, ([^0]), 0',r'1,\\1,1',str(g))));"*2)or g