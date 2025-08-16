def p(g):
 R=range
 n=len(g)
 return[[3if g[i][j]<1and all(any(0<=i+k*a<n and 0<=j+k*b<n and g[i+k*a][j+k*b]==2for k in R(1,n))for a,b in[(-1,0),(1,0),(0,-1),(0,1)])else 0for j in R(n)]for i in R(n)]