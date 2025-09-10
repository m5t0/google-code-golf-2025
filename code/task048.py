def p(g):
 m,n=len(g),len(g[0])
 def f(i,j):
  if m>i>-1<j<n and 0<g[i][j]<9:g[i][j]=9;f(i-1,j);f(i+1,j);f(i,j-1);f(i,j+1);
 for k in range(m*n):
  if g[k//n][k%n]==2:f(k//n,k%n);break
 return[[all(all(w!=2for w in v)for v in g)*8]]