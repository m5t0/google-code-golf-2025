def p(g):
 m,n=len(g),len(g[0]);t=[];r={(k//n,k%n):w for k in range(m*n)if(w:=g[k//n][k%n])};b=[[0]*n for i in range(m)]
 def f(i,j):
  if m>i>-1<j<n and(i,j)in r:s[i-u[0],j-u[1]]=r.pop((i,j));f(i+1,j);f(i-1,j);f(i,j+1);f(i,j-1)
 while r:
  t+=[s:={}];u=min(r);f(*u)
  if len({*s.values()})<2:
   t=t[:-1]
   for v in s:b[u[0]+v[0]][u[1]+v[1]]=1
 for s in t:
  for d in 3,2,1:
   for k in range(m):
    for l in range(-9,n):
     a=[(k+v[0]*d+i//d,l+v[1]*d+i%d,w)for v,w in s.items()for i in range(d*d)]
     if all((m>i>-1<j<n)<1or(g[i][j]<1or(g[i][j]==w)*b[i][j])for i,j,w in a)and[*s.values()].count(2)*d*d==sum(m>i>-1<j<n and g[i][j]==2for i,j,w in a):
      for i,j,w in a:
       if m>i>-1<j<n:g[i][j]=w;b[i][j]=0
 return g