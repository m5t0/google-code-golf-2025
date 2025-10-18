def p(e):
 p,m=zip(*((p,m)for p in range(10)for m in range(10)if e[p][m]))
 for s,t in zip(p,m):
  for z,i in(s,t),(p[0]+t-min(m),min(m)+s-p[0]):
   for z in z,p[0]+p[-1]-z:
    for i in i,min(m)+max(m)-i:e[z][i]=e[s][t]
 return e