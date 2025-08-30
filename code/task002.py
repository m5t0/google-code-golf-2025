def p(g):
 n=len(g);g=[[4-b%2for b in a]for a in g]
 def f(i,j):
  if-1<i<n>j>=0and g[i][j]>3:g[i][j]=0;f(i+1,j);f(i-1,j);f(i,j+1);f(i,j-1)
 for i in range(n):f(i,0);f(i,n-1);f(0,i);f(n-1,i)
 return g