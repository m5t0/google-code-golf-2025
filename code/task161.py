def p(g,r=range):
 m,n=len(g),len(g[0])
 for c in range(10):
  if len(x:=[(i,j)for i in r(m)for j in r(n)if g[i][j]==c])&4and all(i*(m-1-i)*j*(n-1-j)<1for i,j in x):return[[c*((i,0)in x or(0,j)in x)for j in r(n)]for i in r(m)]