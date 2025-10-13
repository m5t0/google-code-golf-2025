def p(n,g=enumerate):
 m,u=[(e,r)for e,r in g(n)for r,a in g(r)if a*(r<len(n)-3>e>3)and all(n[e+m//3][r+m%3]==a*(1-(m//3+m%3)%2)for m in range(9))][0]
 for e,a in g(n):
  for r,a in g(a):
   if a and a-n[m][u]:n[a:=2*m-e+2][r]=n[e][r:=2*u-r+2]=n[a][r]=a
 return n