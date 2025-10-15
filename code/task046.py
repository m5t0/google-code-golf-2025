def p(p):
 r=m=0;n,*o=[*zip(*p)],;n+=[[0]*3]*any(n[-1])
 for e,f in enumerate(n):
  if any(f)^1:
   o+=[[max({*sum(n[r:e],())}-{5})*(f>0)for f in f]for f in[*zip(*p[m:]+p[:m])][r:e]]
   if n[e+1:]:m+=n[e+1].index(5)-n[e-1].index(5);r=e+1
 return[*zip(*o)]