def p(s):
 p=enumerate;r={e+r*1jfor e,s in p(s)for r,s in p(s)if s};s=0
 def p(s):
  if s in r:r.remove(s);p(s-1);p(s-1j);p(s+1j);p(s+1)
 while r:s+=1;p([*r][0])
 return[[0]*e+[8]+[0]*(s-e-1)for e in range(s)]