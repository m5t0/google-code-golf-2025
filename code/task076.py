def p(g,r=range):
 m,n=len(g),len(g[0]);v,*o=[],
 for i in r(m*n):
  if g[x:=i//n][y:=i%n]==2:
   v+=(s:={(0,0)}),;o+=(x,y),
   for _ in r(50):s|={(a,b)for k,l in s for j in r(9)if n>y+(b:=l+j%3-1)>=0<m>x+(a:=k+j//3-1)>=0<g[x+a][y+b]}
 z,w=o[v.index(s:=max(v,key=len))];t=s=[*s]
 for d,(e,f)in zip(v,o):
  for _ in r(8):
   if d<{*s}and all(((i,j)in d)<=(g[e+i][f+j]==g[z+a][w+b])for(i,j),(a,b)in zip(s,t)):
    for(i,j),(a,b)in zip(s,t):g[e+i][f+j]=g[z+a][w+b]
   s=[(-j,i)for i,j in s];(_-3)or(s:=[(-i,j)for i,j in s])
 return g