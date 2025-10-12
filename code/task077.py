def p(g,r=range):
 for _ in r(24):
  for x in r(len(g)-1):
   for y in r(len(g[0])-1):
    if(g[x+1][y]in[2,4])*(g[x][y]-2)*(g[x][y+1]in[2,4]or x*(g[x-1][y]==2)):g[x][y]=4
  *g,=map(list,zip(*g[::-1]))
 return g