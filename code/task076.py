def p(g,r=range):
 m,b=len(g),len(g[0]);k,*o=[],
 for j in r(m*b):
  if g[e:=j//b][y:=j%b]==2:
   k+=(c:={(0,0)}),;o+=(e,y),
   for j in r(50):c|={(a,q)for k,n in c for j in r(9)if b>y+(q:=n+j%3-1)>=0<m>e+(a:=k+j//3-1)>=0<g[e+a][y+q]}
 n,y=o[k.index(c:=max(k,key=len))];t=c
 for s,(e,f)in zip(k,o):
  for j in r(-3,5):
   if s<{*c}and all(((i,j)in s)<=(g[e+i][f+j]==g[n+a][y+q])for(i,j),(a,q)in zip(c,t)):
    for(i,j),(a,q)in zip(c,t):g[e+i][f+j]=g[n+a][y+q]
   c=[(-j,i)for i,j in c];j or(c:=[(-i,j)for i,j in c])
 return g