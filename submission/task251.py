def p(g):
 def f(i,j):
  for k in[-1,1]*(-n<i<n>j>-n<1>g[i][j]):g[i][j]=1;f(i+k,j);f(i,j+k)
 for i in range(n:=len(g)):f(i,0);f(0,i);f(i,-1);f(-1,i)
 return[[[1,0,2][x]for x in v]for v in g]