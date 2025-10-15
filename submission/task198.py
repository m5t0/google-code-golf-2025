import re
p=lambda g,s=re.sub:exec(r"g[:]=zip(*eval(s('3, 4','4,4',s(r'([^34], )3, \1',r'\1 4,\1',s('(([^34], ){2,})3',r'\1 4',s(*'03',str(g))))))[::-1]);"*24)or g