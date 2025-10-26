def p(v,d=enumerate):
 def p(o,t,u,d,r):
  o+=u;t+=d;n=0
  if r>2or not v[o:o+1]or not v[o][t:t+1]or(n:=v[o][t]):return n>5or n==2and 2
  v[o][t]=3;n=p(o,t,u,d,r)
  if n>1or n and(p(o,t,-d,-u,r+1)>1or p(o,t,d,u,r+1)>1):return 2
  v[o][t]=0;return 0
 for(o,t),(n,r)in(r:=[(o,t)for o,n in d(v)for t,n in d(n)if n==3]),r[::-1]:
  if p(o,t,o-n,t-r,0)>1:return v