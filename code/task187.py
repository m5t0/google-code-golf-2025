def p(g):
 m,n=len(g),len(g[0]);g=[[b or 2for b in a]for a in g]
 def f(i,j):
  if n>j>=0<(i<m)and g[i][j]==2:g[i][j]=3;f(i+1,j);f(i-1,j);f(i,j+1);f(i,j-1)
 for i in range(m):f(i,0);f(i,n-1);f(0,i);f(m-1,i)
 return g