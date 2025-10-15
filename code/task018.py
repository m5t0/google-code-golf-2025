def p(o):
 a,m,*e=len(o),len(o[0]);i={(e//m,e%m):sum(o,[])[e]for e in range(a*m)if sum(o,[])[e]}
 def n(f,s):
  if a>f>-1<s<m>0<((f,s)in i):
   r[f-v,s-u]=i.pop((f,s))
   for e in-1,1:n(f+e,s);n(f,s+e)
 while i:
  e+=[r:={}];v,u=min(i);n(v,u)
  if len(r)<4:e.pop()
  else:
   for f,s in r:o[v+f][u+s]=0
 v=eval(str(o))
 for r in e:
  for i in range(8):
   for e in range(a*m):
    if all(a>e//m+l[0]>-1<e%m+l[1]<m for l in r)>0<2<sum(o[e//m+l[0]][e%m+l[1]]==f for l,f in r.items()):
     for l,f in r.items():v[e//m+l[0]][e%m+l[1]]=f
   r={([-n,n][i&3>2],e):f for(e,n),f in r.items()}
 return v