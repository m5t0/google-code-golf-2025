import re
p=lambda g:exec("g[:]=zip(*eval(re.sub('0(?=..8.{19}8,.8)','1',str(g)))[::-1]);"*4)or g