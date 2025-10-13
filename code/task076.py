def p(g,r=range):
 m,q=len(g),len(g[0]);f,*o=[],
 for l in r(m*q):
  if g[e:=l//q][y:=l%q]==2:
   f+=(n:={(0,0)}),;o+=(e,y),
   for l in r(50):n|={(s,b)for f,l in n for h in r(9)if q>y+(b:=l+h%3-1)>=0<m>e+(s:=f+h//3-1)>=0<g[e+s][y+b]}
 z,y=o[f.index(n:=max(f,key=len))];u=n
 for d,(e,f)in zip(f,o):
  for l in r(-3,5):
   if d<{*n}and all(((q,h)in d)<=(g[e+q][f+h]==g[z+s][y+b])for(q,h),(s,b)in zip(n,u)):
    for(q,h),(s,b)in zip(n,u):g[e+q][f+h]=g[z+s][y+b]
   n=[(-h,q)for q,h in n];l or(n:=[(-q,h)for q,h in n])
 return g