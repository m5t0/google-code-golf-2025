def p(o,r=range):
 for i in r(36):
  v,g,p,f=[0]*9,0,i//6+2,i%6+2
  for i in r(25):
   if~((d:=i//5-2)+(t:=i%5-2))%2:g+=o[i:=p+d][n:=f+t]>0;v[s]=v[s:=d*d+t*t]or o[i][n]
  if g>9:
   for i in r(25):o[p+d][f+t]=~((d:=i//5-2)+(t:=i%5-2))%2*v[d*d+t*t]
   return o