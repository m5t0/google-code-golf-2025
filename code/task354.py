def p(g,r=range):
 d=0,1,0,-1,0
 def D(i,j,c):
  if 0<=j<10>i and g[i][j]==5:g[i][j]=c;[D(i+d[I],j+d[I+1],c)for I in r(4)]
 [[D(i,j,s)for i in r(1,10)]for j in r(10)if(s:=g[0][j])]
 return g