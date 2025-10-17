def p(s):
 e,*a={(i,u):r for i,r in enumerate(s)for u,r in enumerate(r)if r},
 def p(i,u):
  if(i,u)in e:[c,r][e.pop((i,u))-1]+=[(i-m,u-n)];p(i,u+1),p(i,u-1),p(i+1,u),p(i-1,u)
 while e:
  c,r=[],[];m,n=next(w for w in e if e[w]==2);p(m,n)
  if c:a,_=c,r;e=dict(sorted(e.items()))
  elif a:
   r=max(r for r in(1,2,3)if s[m+r-1:]and s[0][n+r-1:]and{s[m+w//r][n+w%r]for w in range(r*r)}=={2})
   for i,u in a+_:
    for w in range(r*r):
     if n+u*r+w%r>=0:s[j:=m+i*r+w//r][n+u*r+w%r]=1+((i,u)in _);e.pop((j,n+u*r+w%r),1)
  else:e|={(m+i,n+u):s[m+i][n+u]for i,u in c+r}
 return s