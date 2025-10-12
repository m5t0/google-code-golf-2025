def p(g):
 m,n=len(g),len(g[0]);t=[];r={(t//n,t%n):q for t in range(m*n)if(q:=g[t//n][t%n])};b=[[0]*n for _ in g]
 def z(p,j):
  if m>p>-1<j<n and(p,j)in r:
   s[p-u,j-f]=r.pop((p,j))
   for t in-1,1:z(p,j+t);z(p+t,j)
 while r:
  t+=[s:={}];u,f=min(r);z(u,f)
  if len({*s.values()})<2:
   t.pop()
   for p,j in s:b[u+p][f+j]=1
 for s in t:
  for d in 3,2,1:
   for t in range(m):
    for l in range(-9,n):
     a=[(t+u*d+p//d,l+f*d+p%d,q)for(u,f),q in s.items()for p in range(d*d)]
     if all((m>p>-1<j<n>g[p][j]>1>(g[p][j]==q)*b[p][j])^1for p,j,q in a)*([*s.values()].count(2)*d*d==sum(m>p>-1<j<n>2==g[p][j]for p,j,q in a)):
      for p,j,q in a:
       if-1<j:b[p][j],g[p][j]=0,q
 return g