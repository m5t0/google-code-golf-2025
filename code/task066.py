def p(o,u=enumerate):
 def p(a,e,f,u,r):
  a+=f;e+=u;n=0
  if r>2or not(o[a:a+1]and(d:=o[a])[e:e+1])or(n:=d[e]):return n>5or n==2and 2
  d[e]=3;n=p(a,e,f,u,r)
  if n>1or n and(p(a,e,-u,-f,r+1)>1or p(a,e,u,f,r+1)>1):return 2
  d[e]=0;return 0
 for(a,e),(n,r)in(r:=[(a,e)for a,n in u(o)for e,d in u(n)if d==3]),r[::-1]:
  if p(a,e,a-n,e-r,0)>1:return o