def p(g):
 for k in range(81):
  if 0<(c:=g[i:=k//9][j:=k%9])<3:g[i+c-1][j+1]=g[i+1][j-c+1]=g[i-1][j+c-1]=g[i-c+1][j-1]=6//c+1
 return g