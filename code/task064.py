import re
p=lambda g:[g,exec("g[:]=zip(*eval(re.sub('{1}, {0}(?=[^])]* [^{0}{1}])','{1},{1}',str(g)))[::-1]);".format(*re.findall(r'(.), ((?!\1).), \1',str(g+[*zip(*g)]))[0])*56)][0]