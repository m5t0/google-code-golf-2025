def p(g,r=range):
 h=[[1<<v for v in l]for l in g]
 for I in r(90):
  if g[i:=I//9][j:=I%9]*g[i][j+1]>0:h[i][j]=h[i][j+1]=h[i][j]|h[i][j+1]
 for j in r(10):
  for i in r(9):
   h[i+1][j]|=(x:=h[i][j])
   if g[i][j]>0>=g[i+1][j]:
    for k in r((x-(i>1)).bit_count()):g[i+k+1][j]=3
    break
 return g