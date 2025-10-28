import re
p=lambda g:exec(r"g[:]=zip(*eval(re.sub('.(.*2[^)]*\),)([^28]*\),)(.*8[^2]*)',r'[\2\1\3',str(g)))[::-1]);"*8)or g