def p(n):
 p=enumerate;s={e+1j*t for e,h in p(n)for t,v in p(h)if v};n=0
 def f(n):
  if n in s:s.remove(n);f(n+1);f(n-1);f(n+1j);f(n-1j)
 while s:n+=1;f(next(iter(s)))
 return[[0]*e+[8]+[0]*(n-e-1)for e in range(n)]