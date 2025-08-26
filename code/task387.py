def p(g,r=range):
 u=0;n=len(g)
 for i in r(n):
  v=[j for j,x in enumerate(g[i])if x%5]
  if len(v)==2:
   a,b=v
   for k in r(9):
    if k-4:g[t:=i+k//3-1][a+k%3-1]=g[i][b];g[t][b+k%3-1]=g[i][a]
   for c in r(1,b-a):
    if~min(c,b-a-c)&1:g[i][a+c]=5
   if u<1:
    for c in r(1,u:=(w:=[x for x in r(n)if g[x][a]%5])[3]-w[1]):
     if~min(c,u-c)&1:g[w[1]+c][a]=g[w[1]+c][b]=5
 return g