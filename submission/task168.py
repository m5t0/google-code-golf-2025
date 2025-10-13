import re
p=lambda g:exec(r"g[:]=zip(*eval(re.sub(r'0(?=(.{35})+..([^0]).{28}\2, \2)',r'\2',str(g)))[::-1]);"*4)or g