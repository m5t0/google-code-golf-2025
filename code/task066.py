def p(o,d=enumerate):
 def p(i,n,a,d,e):
  i+=a;n+=d;r=0
  if e>2or not o[i:i+1]or not o[i][n:n+1]or(r:=o[i][n]):return r>5or r==2and 2
  o[i][n]=3;r=p(i,n,a,d,e)
  if r>1or r and(p(i,n,-d,-a,e+1)>1or p(i,n,d,a,e+1)>1):return 2
  o[i][n]=0;return 0
 for(i,n),(r,e)in(e:=[(i,n)for i,r in d(o)for n,f in d(r)if f==3]),e[::-1]:
  if p(i,n,i-r,n-e,0)>1:return o