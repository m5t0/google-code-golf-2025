def p(g):
 d=0,1,0;r=range(len(g)-1)
 def D(i,j):
  if g[i][j]<1:g[i][j]=3;[D(i+d[I],j+d[I+1])for I in(0,1)]
 [D(i+1,j+1)for i in r for j in r if g[i][j+1]==g[i+1][j]>1]
 return[[x*(x-2)for x in v]for v in g]