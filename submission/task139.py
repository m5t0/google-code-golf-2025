def p(g,r=range):
 for k in r(49):
  if all((4in[*zip(*g)][k%7+i][(a:=k//7):a+3])*(4in g[a+i][k%7:k%7+3])for i in r(3)):
   for l in r(9):g[s][t]=g[s:=k//7+l//3][t:=k%7+l%3]or 7
 return g