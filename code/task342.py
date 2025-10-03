def p(g):
 x,y=divmod(sum(g,[]).index(8),10)
 for I in range(100):
  if s:=g[i:=I//10][j:=I%10]:g[i][j],g[x+(i>x)][y+(j>y)]=0,s
 return g