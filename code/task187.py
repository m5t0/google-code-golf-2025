def p(g):
 n=len(g[0]);g=[[b or 2for b in a]for a in g]
 def f(i,j):
  if(i<len(g))*(n>j>-n)and g[i][j]==2:g[i][j]=3;f(i+1,j);f(i-1,j);f(i,j+1);f(i,j-1)
 for i in range(n):f(i,0);f(0,i)
 return g