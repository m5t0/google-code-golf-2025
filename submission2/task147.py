import re
p=lambda g:exec("g[:]=zip(*eval(re.sub('3, [38]','8,8',str(g)))[::-1]);"*4)or g