def p(o,u=enumerate):
 def p(i,s,f,u,r):
  i+=f;s+=u;n=0
  if r>2or not(o[i:i+1]and(d:=o[i])[s:s+1])or(n:=d[s]):return n>5or n==2and 2
  d[s]=3;n=p(i,s,f,u,r)
  if n>1or n and(p(i,s,-u,-f,r+1)>1or p(i,s,u,f,r+1)>1):return 2
  d[s]=0;return 0
 for(i,s),(n,r)in(r:=[(i,s)for i,n in u(o)for s,d in u(n)if d==3]),r[::-1]:
  if p(i,s,i-n,s-r,0)>1:return o