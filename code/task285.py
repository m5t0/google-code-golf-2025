def p(g):
 l=len(g)
 def p(r,s,e,u,a):
  if l>r>0<s<l and g[r][s]==g[e][u]and(r-e,s-u)not in a:
   a|={(r-e,s-u)}
   for o in-1,0,1:
    for t in-1,0,1:p(r+o,s+t,e,u,a)
 for e in range(l-1):
  for u in range(l):
   if len({*g[e][u:u+2]+g[e+1][u:u+2]})>3:
    f=set()
    for d in 1,0,1,0:
     for r in 1,0:
      if g[e+d][u+r]:
       a=set()
       p(e+d,u+r,e+d,u+r,a)
       f|=a
       for o,t in f:g[e+d+o][u+r+t]=g[e+d][u+r]
      f={(o,-t)for o,t in f}
     f={(-o,t)for o,t in f}
 return g