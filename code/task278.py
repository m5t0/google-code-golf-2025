import re
s="g[:]=zip(*eval(re.sub(r'%s',str(g)))[::-1]);"
p=lambda g:exec(s%"2, 2','1,1"*4+s%"0(?=.{%d}1)','3"*6%(2,2,2,2,len(g[0])*3+4,len(g)*3+4)*4+s%"1','2"*4)or g