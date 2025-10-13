def p(q,m=range,e=enumerate):
 f,*x,n=sum(q,[]),10
 for i,r in e(q):
  if(5in r)>i/9<(0in r[(q:=r.index(5)+1):(r:=9-r[::-1].index(5))]):x+=[x for e in m(q,r)if f[x:=i*n+e]<1]
  else:[f==exec("f[n-e[0]+x[0]],f[n]=f[n],0")for e in[[i for i,r in e(f)if r==n]for n in m(n)]if[n-e[0]for n in e]==[n-x[0]for n in x]for n in e];x=[]
 return[f[i*n:][:n]for i in m(n)]