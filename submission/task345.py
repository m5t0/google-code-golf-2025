import re
s=re.sub
p=lambda g:exec("g[:]=eval(s('(?<=5.{31})2, 0','2,2',s('0(?=.{31}2)','2',str(g))));"*9)or g