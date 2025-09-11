def p(g,e=enumerate):
 x,y=[(i,j)for i,v in e(g)for j,w in e(v)if w>2][0]
 for i,v in e(g):
  for j,w in e(v):
   s,t=2*x-i+1,2*y-j+1
   for k,l in(s,j),(i,t),(s,t):
    if w==2:g[k][l]=2
 return g