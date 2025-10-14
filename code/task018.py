def p(v):
 s,m,*e=len(v),len(v[0]);a={(l//m,l%m):sum(v,[])[l]for l in range(s*m)if sum(v,[])[l]}
 def w(n,d):
  if s>n>-1<d<m>0<((n,d)in a):
   r[n-f,d-i]=a.pop((n,d))
   for l in-1,1:w(n+l,d);w(n,d+l)
 while a:
  e+=[r:={}];f,i=min(a);w(f,i)
  if len(r)<4:e.pop()
  else:
   for n,d in r:v[f+n][i+d]=0
 f=eval(str(v))
 for r in e:
  for a in range(8):
   for l in range(s*m):
    if all(s>l//m+p[0]>-1<l%m+p[1]<m for p in r)>0<2<sum(v[l//m+p[0]][l%m+p[1]]==n for p,n in r.items()):
     for p,n in r.items():f[l//m+p[0]][l%m+p[1]]=n
   r={([-w,w][a&3>2],l):n for(l,w),n in r.items()}
 return f