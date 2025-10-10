import re
p=lambda g:exec("g[:]=zip(*eval(re.sub('3, 4','4,4',re.sub(r'([1-25-9],\s)3, \\1',r'\\1 4,\\1',re.sub(r'(([1-25-9],\s){2,})3',r'\\1 4',re.sub('0','3',str(g))))))[::-1]);"*80)or g