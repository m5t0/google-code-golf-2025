def p(g,r=range):
 q=len(g);f=1
 for n in r(4):
  i,h=zip(*((n,h)for n in r(q)for h in r(q)if g[n][h]));i,b,e,d=min(i),max(i),min(h),max(h);n=g[i][e];h=g[i].count(n)
  if(h<g[b].count(n))&f:
   f,h,p=0,e+h//2,d-h//2
   for n in r(b):g[n][h:p+1]=[4]*(p-h+1)
   for n in r(i+1,b):g[n][e+1:d]=[4]*(d-e-1)
   for n in r(i+1):
    if h>=n:g[i-n][h-n]=4
    if p+n<q:g[i-n][p+n]=4
  g=[*map(list,zip(*g[::-1]))]
 return g