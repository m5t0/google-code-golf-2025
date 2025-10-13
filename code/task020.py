def p(f,e=enumerate):
 d,m=zip(*((d,m)for d,a in e(f)for m,r in e(a)if r))
 a=d[0];t=a+d[-1];r=min(m);i=r+max(m)
 for d,m in zip(d,m):
  for u,n in(d,m),(a+m-r,r+d-a):
   for u in u,t-u:
    for n in n,i-n:f[u][n]=max(f[u][n],f[d][m])
 return f