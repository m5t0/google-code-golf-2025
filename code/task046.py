def p(y):
 u=m=0;a,*t=[*zip(*y)],;a+=[[0]*3]*any(a[-1])
 for r,p in enumerate(a):
  if any(p)^1:
   t+=[[max({*sum(a[u:r],())}-{5})*(p>0)for p in p]for p in[*zip(*y[m:]+y[:m])][u:r]]
   if a[r+1:]:m+=a[r+1].index(5)-a[r-1].index(5);u=r+1
 return[*zip(*t)]