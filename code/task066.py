def p(n,a=enumerate):
 def p(i,r,u,a,o):
  i+=u;r+=a;f=0
  if o>2or not(n[i:i+1]and(m:=n[i])[r:r+1])or(f:=m[r]):return f>5or f==2and 2
  m[r]=3;f=p(i,r,u,a,o)
  if f>1or f and(p(i,r,-a,-u,o+1)>1or p(i,r,a,u,o+1)>1):return 2
  m[r]=0;return 0
 for(i,r),(f,o)in(o:=[(i,r)for i,f in a(n)for r,m in a(f)if m==3]),o[::-1]:
  if p(i,r,i-f,r-o,0)>1:return n