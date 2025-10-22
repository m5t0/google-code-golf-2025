def p(g):
 e={};a,b=[],[]
 for i,v in enumerate(g):
  for j,w in enumerate(v):
   if w:e[(i,j)]=w;[a,[]][w-1]+=[(i,j)]
 def D(i,j):
  if(i,j)in e:[a,b][e.pop((i,j))-1]+=[(i,j)];D(i,j+1),D(i,j-1),D(i+1,j),D(i-1,j)
 D(*min(a))
 while e:
  i,j=min(e);n=[n for n in(3,2,1)if[*zip(*g[i:i+n])][j:j+n]==[(2,)*n]*n][0]
  for x,y in a+b:
   for k in range(n):
    for l in range(n):X=i+(x-min(b)[0])*n+k;Y=j+(y-min(b)[1])*n+l;g[X][Y]=(Y>=0)*e.pop((X,Y),1)
 return g