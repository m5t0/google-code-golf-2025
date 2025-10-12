r=range(841)
def p(g):
 for e in r:
  s,i=e//56+1,e//2%28+1;k=r[:29];v,f=[i*[0]for _ in k],1
  for n in r:c=g[y:=n//29][j:=n%29];o=v[y:=(y-e%2*j//6)%s][j%i];f-=c*o*(c!=o);v[y][j%i]=max(c,o)
  if f>0:return[[v[(n-e%2*j//6)%s][j%i]for j in k]for n in k]