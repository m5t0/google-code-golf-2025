def p(n,o=enumerate):
 j,u=[(e,r)for e,r in o(n)for r,i in o(r)if i*(r<len(n)-3>e>3)and all(n[e+j//3][r+j%3]==i*(1-(j//3+j%3)%2)for j in range(9))][0]
 for e,i in o(n):
  for r,i in o(i):
   if i and i-n[j][u]:n[a:=2*j-e+2][r]=n[e][r:=2*u-r+2]=n[a][r]=i
 return n