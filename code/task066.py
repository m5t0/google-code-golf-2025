def p(a,u=enumerate):
 def p(i,t,e,u,m):
  i+=e;t+=u;n=0
  if m>2or not(a[i:i+1]and(o:=a[i])[t:t+1])or(n:=o[t]):return n>5or n==2and 2
  o[t]=3;n=p(i,t,e,u,m)
  if n>1or n and(p(i,t,-u,-e,m+1)>1or p(i,t,u,e,m+1)>1):return 2
  o[t]=0;return 0
 for(i,t),(n,m)in(m:=[(i,t)for i,n in u(a)for t,o in u(n)if o==3]),m[::-1]:
  if p(i,t,i-n,t-m,0)>1:return a