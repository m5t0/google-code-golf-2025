def p(g,r=range(9)):
 for i in r:
  for j in r:
   if 0<(c:=g[i][j])<3:
    g[i+c-1][j+1]=g[i+1][j-c+1]=g[i-1][j+c-1]=g[i-c+1][j-1]=6//c+1
 return g