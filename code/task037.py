def p(g,r=range):
 for k in r(1,10):
  (a,b),(c,d)=[(i,j)for i in r(10)for j in r(10)if g[i][j]==k]or[(0,0)]*2
  for i in r(c-a):g[a+i][b+((b<d)-(d<b))*i]=k
 return g