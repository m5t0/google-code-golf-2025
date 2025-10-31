import re
r=re.sub
p=lambda g:exec("g[:]=zip(*eval(r('0(?=.{31}2)','4',r('0(?=.{28}1)','7',str(g))))[::-1]);"*4)or g