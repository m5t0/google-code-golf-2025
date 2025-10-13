def p(g):
 p,e=len(g),len(g[0]);t=[];r={(u//e,u%e):h for u in range(p*e)if(h:=g[u//e][u%e])};o=[[0]*e for s in g]
 def d(i,j):
  if p>i>-1<j<e and(i,j)in r:
   s[i-v,j-l]=r.pop((i,j))
   for u in-1,1:d(i,j+u);d(i+u,j)
 while r:
  t+=[s:={}];v,l=min(r);d(v,l)
  if len({*s.values()})<2:
   t.pop()
   for i,j in s:o[v+i][l+j]=1
 for s in t:
  for q in 3,2,1:
   for u in range(p):
    for d in range(-9,e):
     z=[(u+v*q+i//q,d+l*q+i%q,h)for(v,l),h in s.items()for i in range(q*q)]
     if all((p>i>-1<j<e>g[i][j]>1>(g[i][j]==h)*o[i][j])^1for i,j,h in z)*([*s.values()].count(2)*q*q==sum(p>i>-1<j<e>2==g[i][j]for i,j,h in z)):
      for i,j,h in z:
       if-1<j:o[i][j],g[i][j]=0,h
 return g