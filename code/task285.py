def p(r):
 def p(o,n,e,d,f):
  if len(r)>o>0<n<len(r) and r[o][n]==r[e][d]and(o-e,n-d)not in f:
   f|={(o-e,n-d)}
   for t in-1,0,1:
    for i in-1,0,1:p(o+t,n+i,e,d,f)
 for e in range(len(r)-1):
  for d in range(len(r)):
   if len({*r[e][d:d+2]+r[e+1][d:d+2]})>3:
    n=set()
    for l in 1,0,1,0:
     for o in 1,0:
      if r[e+l][d+o]:
       f=set()
       p(e+l,d+o,e+l,d+o,f)
       n|=f
       for t,i in n:r[e+l+t][d+o+i]=r[e+l][d+o]
      n={(t,-i)for t,i in n}
     n={(-t,i)for t,i in n}
 return r