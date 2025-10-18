import re
a=", [^0].{25}[^0])"
p=lambda g:exec("g[:]=zip(*eval(re.sub('0(?=((.{32})*.{28}(...){,2}|..)2%s|2(?=%s','%d',str(g)))[::-1]);"%(a,a,sum({*sum(g,[])})-2)*4)or g