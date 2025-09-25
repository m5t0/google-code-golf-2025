def p(g,r=range):
 *h,=zip(*g)
 for k in r(144):
  for l in r(2,12-max(x:=k//12,y:=k%12)):
   for v in(min(g[x][y:(w:=y+l)]+g[z:=x+l][y:w]+[*h[y][x:z]+h[w][x:z]])>4>max(sum((g[i][y+1:w]for i in r(x+1,z)),[])))*g[x+1:z]:v[y+1:w]=[2]*(l-1)
 return g