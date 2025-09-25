def p(g):
 for v in g[1:-1]:v[1:-1]=[x or 4for x in v[1:-1]]
 for _ in g*4:g=[*zip(*eval(str(g).replace('0, 4','0,0'))[::-1])]
 return g