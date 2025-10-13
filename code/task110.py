r=range(841)
def p(g):
 for d in r:
  i,t=d//56+1,d//2%28+1;n=r[:29];e,f=[t*[0]for d in n],1
  for u in r:a=g[p:=u//29][q:=u%29];o=e[u:=(p-d%2*q//6)%i][q%t];f-=a*o*(a!=o);e[u][q%t]=max(a,o)
  if f>0:return[[e[(u-d%2*q//6)%i][q%t]for q in n]for u in n]