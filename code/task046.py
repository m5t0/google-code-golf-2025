def p(p):
 y=e=0;o,*f=[*zip(*p)],;o+=[[0]*3]*any(o[-1])
 for d,n in enumerate(o):
  if any(n)^1:
   f+=[[max({*sum(o[y:d],())}-{5})*(n>0)for n in e]for e in[*zip(*p[e:]+p[:e])][y:d]]
   if o[d+1:]:e+=o[d+1].index(5)-o[d-1].index(5);y=d+1
 return[*zip(*f)]