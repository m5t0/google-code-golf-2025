def p(r,q=range):
 y=0;n=len(r)
 for i in q(n):
  if len(f:=[e for e,u in enumerate(r[i])if u%5])==2:
   m,e=f
   for u in q(9):
    if u-4:r[i+u//3-1][m+u%3-1]=r[i][e];r[i+u//3-1][e+u%3-1]=r[i][m]
   for u in q(1,e-m):
    if min(u,e-m-u)%2==0:r[i][m+u]=5
   if y<1:
    for u in q(1,y:=(f:=[e for e in q(n)if r[e][m]%5])[3]-f[1]):
     if min(u,y-u)%2==0:r[f[1]+u][m]=r[f[1]+u][e]=5
 return r