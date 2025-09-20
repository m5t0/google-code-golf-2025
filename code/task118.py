def p(g,r=range):
 a,b=len(g),len(g[0]);t={(l,n)for l in r(a)for n in r(b)if g[l][n]&2};d=lambda i,l:[i and(d(i[1:],l)or not i[0]&l and d(i[1:],l|i[0])),l][t<=l]
 for n in 2,3:
  if l:=d([l for d in r(a)for i in r(b)for l in[{(l,n)for l in r(-n,n+1)for l,n in[(d+l,i),(d,i+l)]if a>l>-1<n<b}]if min(g[l][n]for l,n in l)&2],set()):
   for l,n in l:g[l][n]+=3*(g[l][n]&1)
   return g