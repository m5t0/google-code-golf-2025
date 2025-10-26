import re
p=lambda g:exec(r"g[:]=zip(*eval(re.sub('[^05],([0, ]*)5',r'\1 5,5',str(g[::-1]))));"*12)or g