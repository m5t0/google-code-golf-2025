r,n=range,29
def p(g):
 for S in r(1568):
  s,t=S//56+1,(S//2)%28+1;v,f=[[0]*t for _ in r(s)],1
  for i in r(n*n):a=g[x:=i//n][y:=i%n];b=v[(w:=x-S%2*y//6)%s][y%t];f-=a*b*(a!=b);v[w%s][y%t]=max(a,b)
  if f>0:return[[v[(i-S%2*j//6)%s][j%t]for j in r(n)]for i in r(n)]