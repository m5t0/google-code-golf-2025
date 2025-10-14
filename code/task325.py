def p(n):
 p=enumerate;r={e+1j*b for e,g in p(n)for b,k in p(g)if k};n=0
 def h(n):
  if n in r:r.remove(n);h(n+1);h(n-1);h(n+1j);h(n-1j)
 while r:n+=1;h(next(iter(r)))
 return[[0]*e+[8]+[0]*(n-e-1)for e in range(n)]