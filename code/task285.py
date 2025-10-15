def p(a):
 l=len(a)
 def p(n,d,o,e,f):
  if l>n>0<d<l and a[n][d]==a[o][e]and(n-o,d-e)not in f:
   f|={(n-o,d-e)}
   for r in-1,0,1:
    for g in-1,0,1:p(n+r,d+g,o,e,f)
 for o in range(l-1):
  for e in range(l):
   if len({*a[o][e:e+2]+a[o+1][e:e+2]})>3:
    d=set()
    for t in 1,0,1,0:
     for n in 1,0:
      if a[o+t][e+n]:
       f=set()
       p(o+t,e+n,o+t,e+n,f)
       d|=f
       for r,g in d:a[o+t+r][e+n+g]=a[o+t][e+n]
      d={(r,-g)for r,g in d}
     d={(-r,g)for r,g in d}
 return a