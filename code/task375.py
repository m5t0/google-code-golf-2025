def p(g):
 for i,v in enumerate(g):v[i]=v[~i]=0
 return g