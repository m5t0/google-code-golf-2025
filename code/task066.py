def p(m,o=enumerate):
 def p(i,a,d,o,e):
  i+=d;a+=o;n=0
  if e>2or not m[i:i+1]or not m[i][a:a+1]or(n:=m[i][a]):return n>5or n==2and 2
  m[i][a]=3;n=p(i,a,d,o,e)
  if n>1or n and p(i,a,-o,-d,e+1)>1or n and p(i,a,o,d,e+1)>1:return 2
  m[i][a]=0;return 0
 for(i,a),(n,e)in(e:=[(i,a)for i,n in o(m)for a,n in o(n)if n==3]),e[::-1]:
  if p(i,a,i-n,a-e,0)>1:return m