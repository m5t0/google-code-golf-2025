def p(s):
 p=enumerate;r={e+1j*r for e,s in p(s)for r,s in p(s)if s};s=0
 def p(s):
  if s in r:r.remove(s);p(s+1);p(s-1);p(s+1j);p(s-1j)
 while r:s+=1;p(next(iter(r)))
 return[[0]*e+[8]+[0]*(s-e-1)for e in range(s)]