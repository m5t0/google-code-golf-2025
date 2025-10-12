import re
s=re.sub
p=lambda g:exec(r"g[:]=zip(*eval(s('3, 4','4,4',s(r'([^034], )3, \1',r'\1 4,\1',s('(([^034], ){2,})3',r'\1 4',s(*'03',str(g))))))[::-1]);"*24)or g