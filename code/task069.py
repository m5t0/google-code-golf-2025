def p(g,e=enumerate):
 h=[(i,j,w)for i,r in e(g)for j,w in e(r)if(w-8)*w];x,y,_=min(h)
 for i,j,_ in h:g[i][j]=0
 for i,r in e(g):
  for j,w in e(r):
   for k,l,z in(w==8)*h:g[i+k-x][j+l-y]=z
 return g