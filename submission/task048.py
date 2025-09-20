def p(g):
 m,n=len(g),len(g[0])
 def f(i,j):
  for k in[-1,1]*(m>i>-1<j<n and 0<g[i][j]<9):g[i][j]=9;f(i+k,j);f(i,j+k)
 for k in range(m*n):
  if g[k//n][k%n]==2:f(k//n,k%n);break
 return[[8*('2'not in"%s"%g)]]