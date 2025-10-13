def p(t):
 r,*c={(h,i):o for h,o in enumerate(t)for i,o in enumerate(o)if o},
 def f(h,i):
  if(h,i)in r:[a,b][r.pop((h,i))-1]+=[(h-m,i-n)];f(h,i+1),f(h,i-1),f(h+1,i),f(h-1,i)
 while r:
  a,b=[],[];m,n=next(p for p in r if r[p]==2);f(m,n)
  if a:c,g=a,b;r=dict(sorted(r.items()))
  elif c:
   d=max(d for d in(1,2,3)if t[m+d-1:]and t[0][n+d-1:]and{t[m+p//d][n+p%d]for p in range(d*d)}=={2})
   for h,i in c+g:
    for p in range(d*d):
     if n+i*d+p%d>=0:t[j:=m+h*d+p//d][n+i*d+p%d]=1+((h,i)in g);r.pop((j,n+i*d+p%d),1)
  else:r|={(m+h,n+i):t[m+h][n+i]for h,i in a+b}
 return t