def p(g):
 h=[*map(list,g)]
 for k in range(81):
  if g[i:=k//9][j:=4+k%9]:
   for l in range(9):h[i-1+l//3][j-1+l%3]=g[l//3][l%3]
 return h