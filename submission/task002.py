def p(g):
 def f(i,j):
  for k in[-1,1]*(g[i%n][j%n]<1):g[i%n][j%n]=4;f(i+k,j);f(i,j+k)
 for i in range(n:=len(g)):f(i,0);f(0,i);f(-1,i)
 return[[x+2^6for x in v]for v in g]