import re
p=lambda g:exec("g[:]=zip(*eval(re.sub('[^05], ((0, )*)5','\g<1>5,5',str(g)))[::-1]);"*12)or g