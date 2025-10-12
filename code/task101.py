def p(g):
 m,n=len(g),len(g[0]);t=[];r={(k//n,k%n):h for k in range(m*n)if(h:=g[k//n][k%n])};c=[[0]*n for s in g]
 def f(i,j):
  if m>i>-1<j<n and(i,j)in r:
   s[i-x,j-u]=r.pop((i,j))
   for k in-1,1:f(i,j+k);f(i+k,j)
 while r:
  t+=[s:={}];x,u=min(r);f(x,u)
  if len({*s.values()})<2:
   t.pop()
   for i,j in s:c[x+i][u+j]=1
 for s in t:
  for q in 3,2,1:
   for k in range(m):
    for f in range(-9,n):
     a=[(k+x*q+i//q,f+u*q+i%q,h)for(x,u),h in s.items()for i in range(q*q)]
     if all((m>i>-1<j<n>g[i][j]>1>(g[i][j]==h)*c[i][j])^1for i,j,h in a)*([*s.values()].count(2)*q*q==sum(m>i>-1<j<n>2==g[i][j]for i,j,h in a)):
      for i,j,h in a:
       if-1<j:c[i][j],g[i][j]=0,h
 return g