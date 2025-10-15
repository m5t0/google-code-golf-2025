import re
p=lambda g:exec(("g[:]=zip(*eval(re.sub('0(?=, 0.{%%d}0, 5)'%%(3*len(g)-2),'%d',str(g)))[::-1]);")*4%(1,3,4,2))or g