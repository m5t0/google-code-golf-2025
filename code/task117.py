def p(g,e=enumerate):
 x,y=[(i,j)for i,r in e(g)for j,v in e(r)if v*(j<len(g)-3>i>3)and all(g[i+k//3][j+k%3]==v*(1-(k//3+k%3)%2)for k in range(9))][0]
 for i,v in e(g):
  for j,w in e(v):
   if w and w-g[x][y]:g[a:=2*x-i+2][j]=g[i][b:=2*y-j+2]=g[a][b]=w
 return g