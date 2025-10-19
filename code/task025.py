import re
s="g[:]=zip(*eval(re.sub(r'%s',str(g)))[::-1]);"
p=lambda g:exec(s%r"(?<!-)(\d)(?=(, -?\1){5})',r'-\1"*4+s%r"-(.), 0([^)]*) \1',r'-\1,-\1\2 0"*8+s%" \d','0"*7+s%"-','")or g