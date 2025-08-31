def p(g,r=range):
 n,m=len(g),len(g[0]);h=list(zip(*g));K=[(0,1),(-1,-2)]
 for i in r(1,n-1):
  for j,k in K:
   if g[i].count(g[i][j])>1:g[i][k]=g[i][j]
 for j in r(1,m-1):
  for p,q in K:
   if h[j].count(g[p][j])>1:g[q][j]=g[p][j]
 return[[[0,g[i][j]][min(i,n-1-i,j,m-1-j)<2]for j in r(m)]for i in r(n)]