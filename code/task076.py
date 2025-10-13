def p(g,r=range):
 m,i=len(g),len(g[0]);f,*k=[],
 for p in r(m*i):
  if g[e:=p//i][y:=p%i]==2:
   f+=(n:={(0,0)}),;k+=(e,y),
   for p in r(50):n|={(c,x)for f,p in n for h in r(9)if i>y+(x:=p+h%3-1)>=0<m>e+(c:=f+h//3-1)>=0<g[e+c][y+x]}
 z,y=k[f.index(n:=max(f,key=len))];u=n
 for a,(e,f)in zip(f,k):
  for p in r(-3,5):
   if a<{*n}and all(((i,h)in a)<=(g[e+i][f+h]==g[z+c][y+x])for(i,h),(c,x)in zip(n,u)):
    for(i,h),(c,x)in zip(n,u):g[e+i][f+h]=g[z+c][y+x]
   n=[(-h,i)for i,h in n];p or(n:=[(-i,h)for i,h in n])
 return g