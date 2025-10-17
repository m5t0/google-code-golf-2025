def p(l):
 s,m,*e=len(l),len(l[0]);r={(e//m,e%m):sum(l,[])[e]for e in range(s*m)if sum(l,[])[e]}
 def p(n,o):
  if s>n>-1<o<m>0<((n,o)in r):
   i[n-f,o-v]=r.pop((n,o))
   for e in-1,1:p(n+e,o);p(n,o+e)
 while r:
  e+=[i:={}];f,v=min(r);p(f,v)
  if len(i)<4:e.pop()
  else:
   for n,o in i:l[f+n][v+o]=0
 f=eval(str(l))
 for i in e:
  for r in range(8):
   for e in range(s*m):
    if all(s>e//m+t[0]>-1<e%m+t[1]<m for t in i)>0<2<sum(l[e//m+t[0]][e%m+t[1]]==n for t,n in i.items()):
     for t,n in i.items():f[e//m+t[0]][e%m+t[1]]=n
   i={([-p,p][r&3>2],e):n for(e,p),n in i.items()}
 return f