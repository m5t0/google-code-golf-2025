def p(g):
 e=enumerate;s={i+1j*j for i,r in e(g)for j,v in e(r)if v};n=0
 def f(z):
  if z in s:s.remove(z);f(z+1);f(z-1);f(z+1j);f(z-1j)
 while s:n+=1;f(next(iter(s)))
 return[[0]*i+[8]+[0]*(n-i-1)for i in range(n)]