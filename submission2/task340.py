def p(g,e=enumerate):
 for i,v in e(g[1:-1],1):
  for j,w in e(v[1:-1],1):
   if w:v[j]=0
   for a,b,c,d in(i,0,i,1),(i,-1,i,-2),(0,j,1,j),(-1,j,-2,j):
    if g[a][b]==w:g[c][d]=w
 return g