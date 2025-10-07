r=range(841)
def p(g):
 for S in r:
  s,t=S//56+1,S//2%28+1;R=r[:29];v,f=[t*[0]for _ in R],1
  for i in r:a=g[x:=i//29][y:=i%29];b=v[u:=(x-S%2*y//6)%s][y%t];f-=a*b*(a!=b);v[u][y%t]=max(a,b)
  if f>0:return[[v[(i-S%2*j//6)%s][j%t]for j in R]for i in R]
  
  
  
p=lambda g,r=range(29):[[g[i%~-len({*sum(g,[])})][j%~-len({*sum(g,[])})]for j in r]for i in r]