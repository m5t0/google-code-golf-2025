import re
s="g[:]=eval(re.sub('%s',str(g)));"+"g[:]=zip(*g[::-1]);"*2
p=lambda g:exec(s%r"0, 0(?=.{28}5, 0.* ([^05]),)',r'0,\1"*5+s%r"0(?=.{34}(\S))',r'\1"*12+s%"5','0")or g