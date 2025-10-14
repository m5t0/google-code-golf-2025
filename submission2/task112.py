def p(g,e=enumerate):
 x,y=[(i,j)for i,v in e(g)for j,w in e(v)if w>2][0]
 for i,v in e(g):
  for j,w in e(v):
   if w==2:g[2*x-i+1][j]=g[i][2*y-j+1]=2
 return g