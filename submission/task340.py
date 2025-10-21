def p(g):
 for _ in[0]*4:
  for v in g[1:-1]:v[1]=v[0]*(v[0]in v[1:])
  *g,=map(list,zip(*g[::-1]))
 for v in g[2:-2]:v[2:-2]=[0]*(len(v)-4)
 return g