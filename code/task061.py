r=range
def p(g):
 for s in r(1,n:=18):
  v,f=[s*[0]for _ in r(s)],1
  for i in r(n*n):a,b=g[x:=i//n][y:=i%n],v[x%s][y%s];f-=a*b*(a!=b);v[x%s][y%s]=max(a,b)
  if f>0:return[[v[i%s][j%s]for j in r(n)]for i in r(n)]