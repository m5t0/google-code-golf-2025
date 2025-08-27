r,n=range,18
def p(g):
 for s in r(1,n):
  v,f=[[0]*s for _ in r(s)],1
  for i in r(n*n):f-=(a:=g[x:=i//n][y:=i%n])*(b:=v[x%s][y%s])*(a!=b);v[x%s][y%s]=max(a,b)
  if f>0:return[[v[i%s][j%s]for j in r(n)]for i in r(n)]