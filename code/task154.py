def p(g):
 s=[[0]*15]*2
 for _ in s*2:
  for k in[0,1]:
   if g[3+k].count(2)>4:g[6+k:4+k:-1]=g[k:k+2];g[k:k+2]=s
  *g,=map(list,zip(*g[::-1]))
 return g