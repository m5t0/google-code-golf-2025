def p(t):
 o,m,*f=len(t),len(t[0]);r={(e//m,e%m):sum(t,[])[e]for e in range(o*m)if sum(t,[])[e]}
 def a(i,p):
  if o>i>-1<p<m>0<((i,p)in r):
   l[i-n,p-s]=r.pop((i,p))
   for e in-1,1:a(i+e,p);a(i,p+e)
 while r:
  f+=[l:={}];n,s=min(r);a(n,s)
  if len(l)<4:f.pop()
  else:
   for i,p in l:t[n+i][s+p]=0
 n=eval(str(t))
 for l in f:
  for r in range(8):
   for e in range(o*m):
    if all(o>e//m+g[0]>-1<e%m+g[1]<m for g in l)>0<2<sum(t[e//m+g[0]][e%m+g[1]]==i for g,i in l.items()):
     for g,i in l.items():n[e//m+g[0]][e%m+g[1]]=i
   l={([-a,a][r&3>2],e):i for(e,a),i in l.items()}
 return n