def p(f,r=range,p=enumerate):
 u,*e,n=sum(f,[]),10
 for m,f in p(f):
  if(5in f)>m/9<(0in f[(i:=f.index(5)+1):(k:=9-f[::-1].index(5))]):e+=[f for l in r(i,k)if u[f:=m*n+l]<1]
  else:[u==exec("u[m-l[0]+e[0]],u[m]=u[m],0")for l in[[m for m,f in p(u)if f==l]for l in r(n)]if[m-l[0]for m in l]==[m-e[0]for m in e]for m in l];e=[]
 return[u[m*n:][:n]for m in r(n)]