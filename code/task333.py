import re
p=lambda g:exec(r"g[:]=zip(*eval(re.sub('3,([0, ]*)0, (.)',r'3,\1\2,\2',str(g)))[::-1]);"*24)or g