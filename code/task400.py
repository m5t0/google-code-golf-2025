def p(g,r=range(5)):
 for i in range(576):
  x,y=i//24,i%24
  if g[x][y]==1:return[[g[x+a].__setitem__(y+b,g[23-x-a][23-y-b])or g[x+a][y+b]for b in r]for a in r]