def p(g,r=range):
 t=len(g);a=[[g[i][j]for j in r(t)if 0<g[i][j]!=5]for i in r(t)if any(0<g[i][j]!=5for j in r(t))]
 for i in r(t):
  for j in r(t):
   if g[i][j]==5:
    for k in r(len(a)):
     for l in r(len(a[0])):g[i+k][j+l]=a[k][l]
 return g