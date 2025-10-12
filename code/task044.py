def p(f,r=range,e=enumerate):
 u,*s,n=sum(f,[]),10
 for m,f in e(f):
  if(5in f)>m/9<(0in f[(x:=f.index(5)+1):(d:=9-f[::-1].index(5))]):s+=[f for o in r(x,d)if u[f:=m*n+o]<1]
  else:[u==exec("u[m-o[0]+s[0]],u[m]=u[m],0")for o in[[m for m,f in e(u)if f==o]for o in r(n)]if[m-o[0]for m in o]==[m-s[0]for m in s]for m in o];s=[]
 return[u[m*n:][:n]for m in r(n)]