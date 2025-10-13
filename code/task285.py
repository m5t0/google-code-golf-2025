def p(t):
 n=len(t)
 def p(f,d,i,g,r):
  if n>f>0<d<n and t[f][d]==t[i][g]and(f-i,d-g)not in r:
   r|={(f-i,d-g)}
   for s in-1,0,1:
    for o in-1,0,1:p(f+s,d+o,i,g,r)
 for i in range(n-1):
  for g in range(n):
   if len({*t[i][g:g+2]+t[i+1][g:g+2]})>3:
    f=set()
    for a in 1,0,1,0:
     for l in 1,0:
      if t[i+a][g+l]:
       r=set()
       p(i+a,g+l,i+a,g+l,r)
       f|=r
       for s,o in f:t[i+a+s][g+l+o]=t[i+a][g+l]
      f={(s,-o)for s,o in f}
     f={(-s,o)for s,o in f}
 return t