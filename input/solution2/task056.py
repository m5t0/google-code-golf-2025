def p(g):
 a=tuple(0if v==0else 1for v in g[0])
 return[[{(1,1,0):1,(1,0,1):2,(0,1,1):3,(0,1,0):6}[a]]]