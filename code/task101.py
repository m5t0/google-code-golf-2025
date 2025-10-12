def p(g):
 m,n=len(g),len(g[0]);t=[];r={(k//n,k%n):w for k in range(m*n)if(w:=g[k//n][k%n])};b=[[0]*n for _ in g]
 def f(i,j):
  if m>i>-1<j<n and(i,j)in r:
   s[i-x,j-y]=r.pop((i,j))
   for k in-1,1:f(i,j+k);f(i+k,j)
 while r:
  t+=[s:={}];x,y=min(r);f(x,y)
  if len({*s.values()})<2:
   t.pop()
   for i,j in s:b[x+i][y+j]=1
 for s in t:
  for d in 3,2,1:
   for k in range(m):
    for l in range(-9,n):
     a=[(k+x*d+i//d,l+y*d+i%d,w)for(x,y),w in s.items()for i in range(d*d)]
     if all((m>i>-1<j<n>g[i][j]>1>(g[i][j]==w)*b[i][j])^1for i,j,w in a)*([*s.values()].count(2)*d*d==sum(m>i>-1<j<n>2==g[i][j]for i,j,w in a)):
      for i,j,w in a:
       if-1<j:b[i][j],g[i][j]=0,w
 return g