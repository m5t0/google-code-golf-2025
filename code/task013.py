import re
s="g[:]=zip(*eval(re.sub(r'%s',str(g))));"
p=lambda g:exec((s%r"\([0, ]*(.)\)',r'(\1,)*len(g[0])"+"g[:]=g[::-1];")*8+s%r"([^0])([, 0]+), ([^0])\2, 0',r'\1\2,\3\2,\1"*22)or g