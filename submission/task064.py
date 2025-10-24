import re
p=lambda g:[g,c:=re.findall(r'(.), ((?!\1).), \1',str(g+[*zip(*g)]))[0],a:=c[0],b:=c[1],exec(f"g[:]=zip(*eval(re.sub('{b}, {a}(?=[^\]\)]* [^{a}{b}])','{b},{b}',str(g)))[::-1]);"*56)][0]