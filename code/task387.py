def p(g,r=range):
 u=0;s=len(g)
 for i in r(s):
  v=[j for j in r(len(g[0]))if g[i][j]%5]
  if 1<len(v)<3:
   for k in-1,0,1:
    for l in-1,0,1:
     if k|l:g[i+k][v[0]+l]=g[i][v[1]];g[i+k][v[1]+l]=g[i][v[0]]
   for c in r(1,v[1]-v[0]):
    if~min(c,v[1]-v[0]-c)&1:g[i][v[0]+c]=5
   w=[x for x in r(s)if g[x][v[0]]%5]
   if not u:
    u=1
    for c in r(1,w[3]-w[1]):
     if~min(c,w[3]-w[1]-c)&1:g[w[1]+c][v[0]]=g[w[1]+c][v[1]]=5
 return g