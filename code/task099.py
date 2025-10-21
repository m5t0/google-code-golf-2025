import re
s="g[:]=zip(*eval(re.sub(r'%s',str(g)))[::-1]);"
p=lambda g:exec(s%r"([^01]), 0',r'\1,\1"*8+s%("0,.{10}0,(?=.{21}1, ([^1]), 1)',r'"+"\\1,"*5)*4)or g