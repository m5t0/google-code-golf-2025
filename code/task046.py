def p(m):
 u=e=0;o,*i=[*zip(*m)],;o+=[[0]*3]*any(o[-1])
 for r,n in enumerate(o):
  if any(n)^1:
   i+=[[max({*sum(o[u:r],())}-{5})*(n>0)for n in e]for e in[*zip(*m[e:]+m[:e])][u:r]]
   if o[r+1:]:e+=o[r+1].index(5)-o[r-1].index(5);u=r+1
 return[*zip(*i)]