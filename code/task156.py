def p(g):
 h=[0,*map(any,g),0];a,b,x,y=[i for i in range(11)if h[i]^h[i+1]]
 for i,(_,a,b,c,d)in enumerate(sorted(((t-s)*((v:=10-g[s][::-1].index(4))-(u:=g[s].index(4))),s,t,u,v)for s,t in((a,b),(x,y)))):
  for v in g[a+1:b-1]:v[c+1:d-1]=[i+1]*(d-c-2)
 return g