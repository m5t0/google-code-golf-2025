def p(n):
 e=enumerate;i={d+1j*i for d,n in e(n)for i,n in e(n)if n};n=0
 def p(n):
  if n in i:i.remove(n);p(n+1);p(n-1);p(n+1j);p(n-1j)
 while i:n+=1;p(next(iter(i)))
 return[[0]*d+[8]+[0]*(n-d-1)for d in range(n)]