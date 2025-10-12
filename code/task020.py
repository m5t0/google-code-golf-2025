def p(g,r=range):
 for s in r(36):
  v,c,p,q=[0]*9,0,s//6+2,s%6+2
  for k in r(25):
   if~((m:=k//5-2)+(n:=k%5-2))%2:c+=g[i:=p+m][j:=q+n]>0;v[x]=v[x:=m*m+n*n]or g[i][j]
  if c>9:
   for k in r(25):g[p+m][q+n]=~((m:=k//5-2)+(n:=k%5-2))%2*v[m*m+n*n]
   return g