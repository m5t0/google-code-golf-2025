def p(g,e=exec):
 n=len(g);m=len(g[0])
 for I in range(n*m):
  if g[i:=I//m][j:=I%m]&5:
   if i<n-1and j<m-1and g[t:=i+1][j]==g[i][u:=j+1]==g[t][u]==5:
    s="g[i][j]=g[t][j]=g[i][u]=g[t][u]=";e(s+"8")
    if p(g):return g
    e(s+"5")
   for x,y in(0,1),(1,0):
    if[i,j][y]<[n,m][y]-2and g[t:=i+x][u:=j+y]==g[t+x][u+y]==5:
     s="g[i][j]=g[t][u]=g[t+x][u+y]=";e(s+"2")
     if p(g):return g
     e(s+"5")
   return 0
 return 1