def p(g,r=range(10)):
 x,y=[(i,j)for i in r for j in r if g[i][j]==8][0]
 for i in r:
  for j in r:
   if s:=g[i][j]:g[i][j],g[x+(i>x)][y+(j>y)]=0,s
 return g