def p(g,a=3):
 A=len(g)>>1
 for B in range(A+1):
  if g[~1][A-B]<1:g[-a][A-B]=g[-a][A+B]=g[~0][A];a+=1
 return g