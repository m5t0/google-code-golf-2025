def p(e,i=enumerate):
 o,m=zip(*((o,m)for o,n in i(e)for m,r in i(n)if r))
 n=o[0];f=n+o[-1];r=min(m);p=r+max(m)
 for o,m in zip(o,m):
  for u,i in(o,m),(n+m-r,r+o-n):
   for u in u,f-u:
    for i in i,p-i:e[u][i]=max(e[u][i],e[o][m])
 return e