def p(g):
 for r in range(4):
  for c in range(4):
   if g[r][c+5]>0:
    g[r][c+10]=g[r][c+5]
   if g[r][c]>0:
    g[r][c+10]=g[r][c]
 g=[R[10:] for R in g]
 return g
