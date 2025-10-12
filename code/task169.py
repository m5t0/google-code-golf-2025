def p(g):
 def f(i,j,b):
  if-1<i<10>j>-1<g[i][j]>4-(b>0):g[i][j]=b or 4;return sum(f(i+k,j,b)+f(i,j+k,b)for k in(-1,1))+1
  return 0
 for k in range(99):x=k//10,k%10;f(*x,5-f(*x,0))
 return g