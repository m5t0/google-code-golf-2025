def p(g):
 for k in{*sum(g,[])}-{0}:
  f=lambda l:[i for i,r in enumerate(l)if k in r];a,b=f(g);c,d=f(zip(*g))
  for v in g[a:b+1]:v[c:d+1]=[k]*(d+1-c)
 return g