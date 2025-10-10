def p(g):
 for _ in'*'*4:
  r=next(r for r in g if 2in r);j=14-r[::-1].index(2)
  if r[j-2]<1:
   for r in g:
    for d in 2,3:r[j+d],r[j-d]=r[j-d],0
  g=[*map(list,zip(*g[::-1]))]
 return g