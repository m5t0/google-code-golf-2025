import re
p=lambda g:exec('g[:]=zip(*eval(re.sub("0(?=.{31}2)","4",re.sub("0(?=.{28}1)","7",str(g))))[::-1]);'*4)or g