def p(g,r=range):
 d=0,1,0,-1,0;n,m=len(g),len(g[0])
 def D(i,j):
  if (0<=i<n)&(0<=j<m)and g[i][j]<1:g[i][j]=3;[D(i+d[I],j+d[I+1])for I in r(4)]
 [[D(i+1,j+1)for i in r(n-1)if g[i][j+1]==g[i+1][j]==g[i][j]==2]for j in r(m-1)]
 return[[[x,0][x==2]for x in v]for v in g]