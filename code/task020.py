def p(a,p=range):
 for n in p(36):
  r,c,j,o=[0]*9,0,n//6+2,n%6+2
  for n in p(25):
   if~((z:=n//5-2)+(g:=n%5-2))%2:c+=a[i:=j+z][e:=o+g]>0;r[n]=r[n:=z*z+g*g]or a[i][e]
  if c>9:
   for n in p(25):a[j+z][o+g]=~((z:=n//5-2)+(g:=n%5-2))%2*r[z*z+g*g]
   return a