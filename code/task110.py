r,n=range,29
def p(g):
 for z in 0,1:
  for s in r(1,n):
   for t in r(1,n):
    v,f=[[0]*t for _ in r(s)],1
    for i in r(n*n):f-=(a:=g[x:=i//n][y:=i%n])*(b:=v[(w:=(x-z*y//6))%s][y%t])*(a!=b);v[w%s][y%t]=max(a,b)
    if f>0:return[[v[(i-z*j//6)%s][j%t]for j in r(n)]for i in r(n)]