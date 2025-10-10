def p(g):
 p=enumerate
 for n in 0,1:
  q=[i for i,r in p(g)if r[0]]
  for q in q:
   for i,e in((i,e)for i,r in p(g)for e,r in p(r)if r&2):
    while(i-q)*(g[i][e]-8):g[i][e]=2;i+=i<q or-1
    if i==q:
     for r in g[q-1:q+2]:r[e-1:e+2]=8,8,8;g[q][e]=2
  h=[*map(list,zip(*g))]
  if q:return(g,h)[n]
  g=h