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

def p(g,r=range,e=enumerate):
 e,v,*o={(i,j):w for i,v in e(g)for j,w in e(v)if w},[]
 def f(u):
  if u in e:
   q[u]=e.pop(u)
   for k in r(9):f((u[0]+k//3-1,u[1]+k%3-1))
 while e:
  q={};f(min(e))
  for a in q:
   if q[a]==2:v+=[{(i-a[0],j-a[1])for i,j in q}];o+=a,
 z,w=o[v.index(s:=max(v,key=len))];t=s=[*s]
 for d,(e,f) in zip(v,o):
  for _ in r(8):
   a=dict(zip(s,t))
   if d<{*s}and all(g[e+i][f+j]==g[z+a[i,j][0]][w+a[i,j][1]]for i,j in d):
    for(i,j),(u,v)in a.items():g[e+i][f+j]=g[z+u][w+v]
   s=[(-j,i)for i,j in s];(_-3)or(s:=[(-i,j)for i,j in s])
 return g