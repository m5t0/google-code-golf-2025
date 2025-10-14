def p(i):
 f=d=0;a,*t=[*zip(*i)],;a+=[[0]*3]*any(a[-1])
 for m,p in enumerate(a):
  if any(p)^1:
   t+=[[max({*sum(a[f:m],())}-{5})*(p>0)for p in p]for p in[*zip(*i[d:]+i[:d])][f:m]]
   if a[m+1:]:d+=a[m+1].index(5)-a[m-1].index(5);f=m+1
 return[*zip(*t)]