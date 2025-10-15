import re
p=lambda g:exec(r"g[:]=zip(*eval(re.sub(r'0(?=(, 0)*, ([^0])(, \2)*, ((?!\2).), 0)',r'\4',str(g)))[::-1]);"*4)or g