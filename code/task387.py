def p(r):
 (a,t),*s,(u,e)=m=[(u,m)for u,e in enumerate(r)for m,i in enumerate(e)if i]
 for f,(u,m) in enumerate(m):
  for n in-1,0,1:
   for i in-1,0,1:
    if n|i:r[u+n][m+i]=r[a][[e,t][0<f<3]]
 for m in range(2,(u-a)//2+1,2):
  for n in t,e:r[a+m][n]=r[u-m][n]=5
 for m in range(2,(e-t)//2+1,2):
  for n in a,u:r[n][t+m]=r[n][e-m]=5
 return r