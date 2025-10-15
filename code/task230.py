import re
p=lambda g:exec(("g[:]=zip(*eval(re.sub(r'0(?=, 0.{"+str(3*len(g)-2)+"}0, 5)','%d',str(g)))[::-1]);")*4%(1,3,4,2))or g