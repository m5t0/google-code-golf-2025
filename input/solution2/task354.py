def p(g):
 R=range
 r=[x[:]for x in g]
 def d(i,j,c):
  if 0<=i<10 and 0<=j<10 and r[i][j]==5:r[i][j]=c;[d(i+a,j+b,c)for a,b in[(-1,0),(1,0),(0,-1),(0,1)]]
 [[d(i,j,g[0][j])for i in R(1,10)if r[i][j]==5]for j in R(10)if g[0][j]]
 return r