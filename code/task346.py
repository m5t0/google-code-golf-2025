import re
p=lambda g:[[int(re.findall(r'(([^0],) \2 \2).*((?!\2)[^0]), \2.*\1',str(g))[0][2])]]