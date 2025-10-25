import re
p=lambda g,k=7:-k*g or p(eval(re.sub('2\)(.*), \([^3)]*\)((, \(.*?3.*?\))+)',r'2)\2,[8]*len(g)\1',str([*zip(*g)])))[::-1],k-1)