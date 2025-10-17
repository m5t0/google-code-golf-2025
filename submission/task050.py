import re
p=lambda g:exec("g[:]=zip(*eval(re.sub('(8(, 3)*, )0((, 0)*, 8)','\g<1>3\g<3>',str(g))));"*24)or g
