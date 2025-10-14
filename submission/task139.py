import re
p=lambda g:exec("g[:]=zip(*eval(re.sub('0(?=(..[47].{25}[47]))','7',str(g)))[::-1]);"*12)or g