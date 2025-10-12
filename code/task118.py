def p(f,r=range):
 a,b=len(f),len(f[0]);e={(l,n)for l in r(a)for n in r(b)if f[l][n]&2};t=lambda i,l:[i and(t(i[1:],l)or not i[0]&l and t(i[1:],l|i[0])),l][e<=l]
 for n in 2,3:
  if l:=t([l for t in r(a)for i in r(b)for l in[{(l,n)for l in r(-n,n+1)for l,n in[(t+l,i),(t,i+l)]if a>l>-1<n<b}]if min(f[l][n]for l,n in l)&2],set()):
   for l,n in l:f[l][n]+=3*(f[l][n]&1)
   return f