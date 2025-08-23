def p(g,e=exec):
 n=len(g);m=len(g[0]);s="g[i][j]=g[v][w]=g[v"
 for I in range(n*m):
  if g[i:=I//m][j:=I%m]&5:
   if i<n-1and j<m-1and g[v:=i+1][j]==g[i][w:=j+1]==g[v][w]==5:
    t=s+"][j]=g[i][w]=";e(t+"8")
    if p(g):return g
    e(t+"5")
   for x,y in(0,1),(1,0):
    if[i,j][y]<[n,m][y]-2and g[v:=i+x][w:=j+y]==g[v+x][w+y]==5:
     t=s+"+x][w+y]=";e(t+"2")
     if p(g):return g
     e(t+"5")
   return 0
 return 1