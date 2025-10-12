def p(g,r=range):
 m,i=len(g),len(g[0]);f,*o=[],
 for l in r(m*i):
  if g[e:=l//i][y:=l%i]==2:
   f+=(n:={(0,0)}),;o+=(e,y),
   for l in r(50):n|={(u,c)for k,l in n for h in r(9)if i>y+(c:=l+h%3-1)>=0<m>e+(u:=k+h//3-1)>=0<g[e+u][y+c]}
 z,w=o[f.index(n:=max(f,key=len))];t=n
 for d,(e,f)in zip(f,o):
  for l in r(-3,5):
   if d<{*n}and all(((i,h)in d)<=(g[e+i][f+h]==g[z+u][w+c])for(i,h),(u,c)in zip(n,t)):
    for(i,h),(u,c)in zip(n,t):g[e+i][f+h]=g[z+u][w+c]
   n=[(-h,i)for i,h in n];l or(n:=[(-i,h)for i,h in n])
 return g