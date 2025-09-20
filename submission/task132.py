def p(g,r=range):
 for k in{*sum(g,[])}-{0}:
  f=lambda l:sorted(i for i in r(len(l))if k in l[i]);a,b=f(g);c,d=f([*zip(*g)])
  for v in g[a:b+1]:v[c:d+1]=[k]*(d+1-c)
 return g;