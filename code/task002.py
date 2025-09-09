def p(g):
 n=len(g);g=[[4-b%2for b in a]for a in g]
 def f(i,j):
  if-n<i<n>j>-n and g[i][j]>3:g[i][j]=0;f(i+1,j);f(i-1,j);f(i,j+1);f(i,j-1)
 for i in range(n):f(i,0);f(0,i);f(-1,i)
 return g