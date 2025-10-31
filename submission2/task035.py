import re
p=lambda g:exec(r"g[:]=zip(*eval(re.sub('8([0, ]{3,})([1-9])',r'\2\1\2',str(g)))[::-1]);"*4)or g