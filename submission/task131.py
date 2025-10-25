import re
p=lambda g:exec(r"g[:]=zip(*eval(re.sub('2\)(.*), \([^3)]*\)((, \([^)]*3[^)]*\))+)',r'2)\2,[8]*len(g[0])\1',str(g)))[::-1]);"*8)or g