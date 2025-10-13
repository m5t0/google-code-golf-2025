def p(g):
 R=range
 for s in R(1,5):
  for i in R(1,12-s):
   for j in R(1,12-s):
    if all(g[i-1][x]==g[i+s][x]==5 for x in R(j,j+s))and all(g[y][j-1]==g[y][j+s]==5 for y in R(i,i+s))and sum(g[y][x]for y in R(i,i+s)for x in R(j,j+s))<1:
     for y in R(i,i+s):g[y][j:j+s]=[2]*s
 return g
