def p(g,r=range):
 e,n=len(g),len(g[0])
 for l in r(1,10):
  h,o=l//3,l%3
  if all((e[l]<1)^(p[l+o]>0)for e,p in zip(g,g[h:])for l in r(n-o)):
   e=[e+[0]*(10-n)for e in g]+[[0]*10for p in r(10-e)]
   for l in r(100):e[n][l]=e[n:=l//10][l:=l%10]or(n-h>-1<l-o)*e[n-h][l-o]
   return e