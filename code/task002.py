def p(g):
 n=len(g)
 def f(i,j):
  if-n<i<n>j>-n and g[i][j]<1:g[i][j]=4;[f(i+k,j)==f(i,j+k)for k in[-1,1]]
 for i in range(n):f(i,0);f(0,i);f(-1,i)
 return[[(x+2)^6for x in v]for v in g]