import re
p=lambda g:exec(r"g[:]=zip(*eval(re.sub(r'0(?=(.{22,25}|.{42,45})([^0]), ((?!\2)[^0]).{19}(\d))',r'\4',str(g)))[::-1]);"*4)or g