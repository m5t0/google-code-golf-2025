def p(g,e=enumerate):
 x,y=[(i,j)for i,v in e(g)for j,w in e(v)if w*(j<len(g)-3>i>3)and all(g[i+k//3][j+k%3]==w*(1-(k//3+k%3)%2)for k in range(9))][0]
 for i,v in e(g):
  for j,w in e(v):
   s,t=2*x-i+2,2*y-j+2
   for k,l in(s,j),(i,t),(s,t):
    if w and w!=g[x][y]:g[k][l]=w
 return g