def p(g):
 for k in range(81):
  if g[k//9][k%9]==5:
   for l in range(9):
    if l!=4:g[k//9+l//3-1][k%9+l%3-1]=1
 return g