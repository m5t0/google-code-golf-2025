def p(g,r=range):
 m,b=len(g),len(g[0]);l,*o=[],
 for j in r(m*b):
  if g[p:=j//b][y:=j%b]==2:
   l+=(c:={(0,0)}),;o+=(p,y),
   for j in r(50):c|={(a,q)for l,n in c for j in r(9)if b>y+(q:=n+j%3-1)>=0<m>p+(a:=l+j//3-1)>=0<g[p+a][y+q]}
 n,y=o[l.index(c:=max(l,key=len))];t=c
 for h,(p,f)in zip(l,o):
  for j in r(-3,5):
   if h<{*c}and all(((l,j)in h)<=(g[p+l][f+j]==g[n+a][y+q])for(l,j),(a,q)in zip(c,t)):
    for(l,j),(a,q)in zip(c,t):g[p+l][f+j]=g[n+a][y+q]
   c=[(-j,l)for l,j in c];j or(c:=[(-l,j)for l,j in c])
 return g