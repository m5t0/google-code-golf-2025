def p(g):
 r=range;R=r(n:=len(g));m=[i+1for i in R if g[0][i]or g[i][2]][0];h=[7*[3]for _ in r(7)]
 for k in r(n//m):
  for i in R:
   for x,y,z,v,s,t in(l:=m*-~k-1,i,k,i//m,1,0),(i,l,i//m,k,0,1):
    if g[x][y]<1:g[x][y]=4;exec("if-~i%m:h[z][v]=h[z+s][v+t]=4")
 return[[g[i][j]or h[i//m][j//m]for j in R]for i in R]