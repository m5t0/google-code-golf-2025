def p(g,r=range):
 m,n=len(g),len(g[0]);h=[[0]*(n+2)for _ in r(m+2)]
 for k in r(m*n):
  v=h[1+i][1+j]=g[i:=k//n][j:=k%n]
  for l in[1,3,5,7]*v:
   if((0<(x:=i+l//3)<m+1)*(n+1>(y:=j+l%3)>0))^1:h[x][y]=v
 return h