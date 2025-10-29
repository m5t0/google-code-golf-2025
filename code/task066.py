def p(a):
 def p(i,r,e,u,o):
  i+=e;r+=u;n=0
  if o>2or not a[i:i+1]or not a[i][r:r+1]or(n:=a[i][r]):return n>5or n==2and 2
  a[i][r]=3;n=p(i,r,e,u,o)
  if n>1or n and p(i,r,-u,-e,o+1)>1or n and p(i,r,u,e,o+1)>1:return 2
  a[i][r]=0;return 0
 for(i,r),(n,o)in(o:=[(i,r)for i,n in enumerate(a)for r,n in enumerate(n)if n==3]),o[::-1]:
  if p(i,r,i-n,r-o,0)>1:return a