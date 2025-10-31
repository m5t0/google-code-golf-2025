def p(n):
 f=sum(n,[]);r=sorted({*f},key=f.count)
 for o in r:
  d=[[[r[-1],l][l==o]for*f,l in zip(*n,f)if o in f]for f in n if o in f]
  for l in r:
   for p in range(-22,22):
    for s in range(-22,22):
     if all(t:=[((n[p+r][s+f]==l)==(d[r//2][f//2]==o))*n[p+r][s+f]for r in range(len(d)*2)for f in range(len(d[0])*2)if len(n)>p+r>-1<s+f<len(n[0])])>0<t.count(l)==f.count(l):return d