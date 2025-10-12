def p(f,r=range,e=enumerate):
 u,*s,n=sum(f,[]),10
 for m,f in e(f):
  if(5in f)>m/9<(0in f[(i:=f.index(5)+1):(x:=9-f[::-1].index(5))]):s+=[f for l in r(i,x)if u[f:=m*n+l]<1]
  else:[u==exec("u[m-l[0]+s[0]],u[m]=u[m],0")for l in[[m for m,f in e(u)if f==l]for l in r(n)]if[m-l[0]for m in l]==[m-s[0]for m in s]for m in l];s=[]
 return[u[m*n:][:n]for m in r(n)]