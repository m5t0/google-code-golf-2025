r=range
def p(g):
 for S in r(1568):
  s,t=S//56+1,(S//2)%28+1;R=r(29);v,f=[t*[0]for _ in R],1
  for i in r(841):a=g[x:=i//29][y:=i%29];w=x-S%2*y//6;b=v[w%s][y%t];f-=a*b*(a!=b);v[w%s][y%t]=max(a,b)
  if f>0:return[[v[(i-S%2*j//6)%s][j%t]for j in R]for i in R]