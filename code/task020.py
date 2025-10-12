def p(a,p=range):
 for n in p(36):
  r,c,x,f=[0]*9,0,n//6+2,n%6+2
  for n in p(25):
   if~((o:=n//5-2)+(n:=n%5-2))%2:c+=a[i:=x+o][t:=f+n]>0;r[n]=r[n:=o*o+n*n]or a[i][t]
  if c>9:
   for n in p(25):a[x+o][f+n]=~((o:=n//5-2)+(n:=n%5-2))%2*r[o*o+n*n]
   return a