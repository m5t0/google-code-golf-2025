def p(g,r=range):
 o=len(g);j=1
 for i in r(4):
  s,h=zip(*((i,l)for i in r(o)for l in r(o)if g[i][l]));s,x,e,d=min(s),max(s),min(h),max(h);i=g[s][e];l=g[s].count(i)
  if(l<g[x].count(i))&j:
   j,h,p=0,e+l//2,d-l//2
   for i in r(x):g[i][h:p+1]=[4]*(p-h+1)
   for i in r(s+1,x):g[i][e+1:d]=[4]*(d-e-1)
   for i in r(s+1):
    if h>=i:g[s-i][h-i]=4
    if p+i<o:g[s-i][p+i]=4
  g=[*map(list,zip(*g[::-1]))]
 return g