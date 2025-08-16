def p(g):
 n=len(g);r=range(n);v=[[1]*n for _ in r]
 def f(i,j):
  if(0<=i<n)*(0<=j<n)and v[i][j]*(g[i][j]<1):v[i][j]=0;f(i+1,j);f(i-1,j);f(i,j+1);f(i,j-1)
 for i in r:f(i,0);f(i,n-1);f(0,i);f(n-1,i)
 return[[4 if(g[i][j]<1)*v[i][j] else g[i][j]for j in r]for i in r]