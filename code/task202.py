import re
s="g[:]=zip(*eval(re.sub(r'%s',str(g)))[::-1]);"
p=lambda g:exec(s%r"([^0])(?=[^\]]*0[^\]]*([^0, \]\1]))','0"*4)or g