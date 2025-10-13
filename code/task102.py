def p(g):
 u=range
 for a in u(1,5):
  for i in u(1,12-a):
   for n in u(1,12-a):
    if all(g[i-1][e]==g[i+a][e]==5 for e in u(n,n+a))and all(g[m][n-1]==g[m][n+a]==5 for m in u(i,i+a))and sum(g[m][e]for m in u(i,i+a)for e in u(n,n+a))<1:
     for m in u(i,i+a):g[m][n:n+a]=[2]*a
 return g