def p(g,r=range):
 for s in r(36):
  v,c,p,q=[0]*9,0,s//6+2,s%6+2
  for k in r(25):
   if((m:=k//5-2)+(n:=k%5-2))%2<1:c+=(g[i:=p+m][j:=q+n]>0);v[x]=max(v[x:=m*m+n*n],g[i][j])
  if c>9:break
 for k in r(25):
  g[p+m][q+n]=v[(m:=k//5-2)**2+(n:=k%5-2)**2]*((m+n)%2<1)
 return g