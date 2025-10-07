def p(g,r=range(21)):
 m=min(i for i in r[1:]if g[0][:i]==g[0][i:2*i])
 return[[m]]