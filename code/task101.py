def p(t):
 r,*x={(h,i):o for h,o in enumerate(t)for i,o in enumerate(o)if o},
 def f(h,i):
  if(h,i)in r:[a,e][r.pop((h,i))-1]+=[(h-m,i-n)];f(h,i+1),f(h,i-1),f(h+1,i),f(h-1,i)
 while r:
  a,e=[],[];m,n=next(p for p in r if r[p]==2);f(m,n)
  if a:x,w=a,e;r=dict(sorted(r.items()))
  elif x:
   d=max(d for d in(1,2,3)if t[m+d-1:]and t[0][n+d-1:]and{t[m+p//d][n+p%d]for p in range(d*d)}=={2})
   for h,i in x+w:
    for p in range(d*d):
     if n+i*d+p%d>=0:t[s:=m+h*d+p//d][n+i*d+p%d]=1+((h,i)in w);r.pop((s,n+i*d+p%d),1)
  else:r|={(m+h,n+i):t[m+h][n+i]for h,i in a+e}
 return t