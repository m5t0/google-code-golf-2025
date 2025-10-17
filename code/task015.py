import re
p=lambda g:exec('w=re.sub;g[:]=zip(*eval(w("0(?=.{31}2)","4",w("0(?=.{28}1)","7",str(g))))[::-1]);'*4)or g