def p(h):
 e=enumerate;r={f+1j*r for f,h in e(h)for r,h in e(h)if h};h=0
 def p(h):
  if h in r:r.remove(h);p(h+1);p(h-1);p(h+1j);p(h-1j)
 while r:h+=1;p(next(iter(r)))
 return[[0]*f+[8]+[0]*(h-f-1)for f in range(h)]