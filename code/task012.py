r=range;s=r(2,10)
def p(g):
 for i in s:
  for j in s:
   if c:=g[i][j]*((n:=g[i+1][j])==g[i-1][j]==g[i][j+1]>0):
    for a in r(-2,3):g[i-a][j]=g[i][j-a]=n;g[i+a][j+a]=g[i+a][j-a]=c
 return g