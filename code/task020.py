def p(e,i=enumerate):
 p,m=zip(*((p,m)for p,n in i(e)for m,r in i(n)if r))
 n=p[0];u=n+p[-1];r=min(m);f=r+max(m)
 for p,m in zip(p,m):
  for z,i in(p,m),(n+m-r,r+p-n):
   for z in z,u-z:
    for i in i,f-i:e[z][i]=e[p][m]
 return e