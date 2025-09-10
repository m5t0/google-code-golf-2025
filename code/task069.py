def p(g,e=enumerate):
 h=[(i,j,w)for i,v in e(g)for j,w in e(v)if w*(w-8)];x,y,_=min(h)
 for i,v in e(g):
  for j,w in e(v):
   if(i,j,w)in h:g[i][j]=0
   elif w==8:
    for k,l,z in h:g[i+k-x][j+l-y]=z
 return g