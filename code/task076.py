def p(g,r=range):
 m,i=len(g),len(g[0]);f,*k=[],
 for z in r(m*i):
  if g[e:=z//i][y:=z%i]==2:
   f+=(n:={(0,0)}),;k+=(e,y),
   for z in r(50):n|={(c,x)for f,z in n for h in r(9)if i>y+(x:=z+h%3-1)>=0<m>e+(c:=f+h//3-1)>=0<g[e+c][y+x]}
 b,y=k[f.index(n:=max(f,key=len))];l=n
 for q,(e,f)in zip(f,k):
  for z in r(-3,5):
   if q<{*n}and all(((i,h)in q)<=(g[e+i][f+h]==g[b+c][y+x])for(i,h),(c,x)in zip(n,l)):
    for(i,h),(c,x)in zip(n,l):g[e+i][f+h]=g[b+c][y+x]
   n=[(-h,i)for i,h in n];z or(n:=[(-i,h)for i,h in n])
 return g