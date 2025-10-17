def p(f):
 e,*r={(o,t):n for o,n in enumerate(f)for t,n in enumerate(n)if n},
 def p(o,t):
  if(o,t)in e:[i,n][e.pop((o,t))-1]+=[(o-l,t-m)];p(o,t+1),p(o,t-1),p(o+1,t),p(o-1,t)
 while e:
  i,n=[],[];l,m=next(g for g in e if e[g]==2);p(l,m)
  if i:r,_=i,n;e=dict(sorted(e.items()))
  elif r:
   n=max(n for n in(1,2,3)if f[l+n-1:]and f[0][m+n-1:]and{f[l+g//n][m+g%n]for g in range(n*n)}=={2})
   for o,t in r+_:
    for g in range(n*n):
     if m+t*n+g%n>=0:f[u:=l+o*n+g//n][m+t*n+g%n]=1+((o,t)in _);e.pop((u,m+t*n+g%n),1)
  else:e|={(l+o,m+t):f[l+o][m+t]for o,t in i+n}
 return f