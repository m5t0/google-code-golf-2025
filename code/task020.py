def p(r,p=range):
 for i in p(36):
  e,g,n,f=[0]*9,0,i//6+2,i%6+2
  for i in p(25):
   if~((a:=i//5-2)+(t:=i%5-2))%2:g+=r[i:=n+a][j:=f+t]>0;e[a]=e[a:=a*a+t*t]or r[i][j]
  if g>9:
   for i in p(25):r[n+a][f+t]=~((a:=i//5-2)+(t:=i%5-2))%2*e[a*a+t*t]
   return r