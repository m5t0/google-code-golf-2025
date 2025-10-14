def p(r,d=range):
 l=0;n=len(r)
 for g in d(n):
  if len(f:=[e for e,u in enumerate(r[g])if u%5])==2:
   m,e=f
   for u in d(9):
    if u-4:r[g+u//3-1][m+u%3-1]=r[g][e];r[g+u//3-1][e+u%3-1]=r[g][m]
   for u in d(1,e-m):
    if min(u,e-m-u)%2==0:r[g][m+u]=5
   if l<1:
    for u in d(1,l:=(f:=[e for e in d(n)if r[e][m]%5])[3]-f[1]):
     if min(u,l-u)%2==0:r[f[1]+u][m]=r[f[1]+u][e]=5
 return r