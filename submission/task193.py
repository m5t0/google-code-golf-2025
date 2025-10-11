import re
p=lambda g:exec("g[:]=zip(*eval(re.sub(r'0, [1-9](, 0|\))',r'0,0\\1',str(g)))[::-1]);"*8)or g