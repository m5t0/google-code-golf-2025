def p(g,e=enumerate):
 x,y,_=min(h:=[(i,j,w)for i,r in e(g)for j,w in e(r)if(w-8)*w])
 for i,j,_ in h:g[i][j]=0
 for i,r in e(g):
  for j,w in e(r):
   for k,l,z in(w==8)*h:g[i+k-x][j+l-y]=z
 return g