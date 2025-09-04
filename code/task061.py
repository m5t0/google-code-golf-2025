r=range
def p(g):
 for s in r(1,n:=18):
  R=r(n);v,f=[s*[0]for _ in R],1
  for i in r(n*n):a,b=g[x:=i//n][y:=i%n],v[x%s][y%s];f-=a*b*(a!=b);v[x%s][y%s]=max(a,b)
  if f>0:return[[v[i%s][j%s]for j in R]for i in R]