def p(g,r=range):
 u=0;n=len(g)
 for i in r(n):
  if len(v:=[j for j,c in enumerate(g[i])if c%5])==2:
   a,b=v
   for c in r(9):
    if c-4:g[i+c//3-1][a+c%3-1]=g[i][b];g[i+c//3-1][b+c%3-1]=g[i][a]
   for c in r(1,b-a):
    if min(c,b-a-c)%2==0:g[i][a+c]=5
   if u<1:
    for c in r(1,u:=(w:=[x for x in r(n)if g[x][a]%5])[3]-w[1]):
     if min(c,u-c)%2==0:g[w[1]+c][a]=g[w[1]+c][b]=5
 return g