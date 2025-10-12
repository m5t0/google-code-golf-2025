def p(g,r=range):
 f,u=len(g),len(g[0]);d={(l,n)for l in r(f)for n in r(u)if g[l][n]&2};m=lambda i,l:[i and(m(i[1:],l)or not i[0]&l and m(i[1:],l|i[0])),l][d<=l]
 for n in 2,3:
  if l:=m([l for m in r(f)for i in r(u)for l in[{(l,n)for l in r(-n,n+1)for l,n in[(m+l,i),(m,i+l)]if f>l>-1<n<u}]if min(g[l][n]for l,n in l)&2],set()):
   for l,n in l:g[l][n]+=3*(g[l][n]&1)
   return g