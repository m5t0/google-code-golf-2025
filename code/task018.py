def p(p):
 m,d,*f=len(p),len(p[0]);r={(e//d,e%d):sum(p,[])[e]for e in range(m*d)if sum(p,[])[e]}
 def a(i,z):
  if m>i>-1<z<d>0<((i,z)in r):
   l[i-n,z-s]=r.pop((i,z))
   for e in-1,1:a(i+e,z);a(i,z+e)
 while r:
  f+=[l:={}];n,s=min(r);a(n,s)
  if len(l)<4:f.pop()
  else:
   for i,z in l:p[n+i][s+z]=0
 n=eval(str(p))
 for l in f:
  for r in range(8):
   for e in range(m*d):
    if all(m>e//d+g[0]>-1<e%d+g[1]<d for g in l)>0<2<sum(p[e//d+g[0]][e%d+g[1]]==i for g,i in l.items()):
     for g,i in l.items():n[e//d+g[0]][e%d+g[1]]=i
   l={([-a,a][r&3>2],e):i for(e,a),i in l.items()}
 return n