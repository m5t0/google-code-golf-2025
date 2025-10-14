def p(g):
 for _ in[0]*4:
  for k in 0,1:
   if g[3+k].count(2)>4:g[k:k+2]=g[6+k:4+k:-1];g[5+k:7+k]=[[0]*15]*2
  *g,=zip(*g[::-1])
 return g