def p(g):
 n=len(g)
 def f(x,y,i,j,c):
  if n>x>0<y<n and g[x][y]==g[i][j]and(x-i,y-j)not in c:
   c|={(x-i,y-j)}
   for s in-1,0,1:
    for t in-1,0,1:f(x+s,y+t,i,j,c)
 for i in range(n-1):
  for j in range(n):
   if len({*g[i][j:j+2]+g[i+1][j:j+2]})>3:
    b=set()
    for k in 1,0,1,0:
     for l in 1,0:
      if g[i+k][j+l]:
       c=set()
       f(i+k,j+l,i+k,j+l,c)
       b|=c
       for s,t in b:g[i+k+s][j+l+t]=g[i+k][j+l]
      b={(s,-t)for s,t in b}
     b={(-s,t)for s,t in b}
 return g