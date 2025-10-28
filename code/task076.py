def p(q):
 f,h=len(q),len(q[0]);r,*k=[],
 for m in range(f*h):
  if q[p:=m//h][d:=m%h]==2:
   r+=(a:={(0,0)}),;k+=(p,d),
   for m in range(50):a|={(o,l)for r,e in a for m in range(9)if h>d+(l:=e+m%3-1)>=0<f>p+(o:=r+m//3-1)>=0<q[p+o][d+l]}
 e,d=k[r.index(a:=max(r,key=len))];j=a
 for z,(p,f)in zip(r,k):
  for m in range(-3,5):
   if z<{*a}and all(((r,m)in z)<=(q[p+r][f+m]==q[e+o][d+l])for(r,m),(o,l)in zip(a,j)):
    for(r,m),(o,l)in zip(a,j):q[p+r][f+m]=q[e+o][d+l]
   a=[(-m,r)for r,m in a];m or(a:=[(-r,m)for r,m in a])
 return q