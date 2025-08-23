def p(g):
 r,m,n=range,len(g),len(g[0]);o=[[0]*n for _ in r(m)]
 for s in r(m*n):
  if c:=g[i:=s//n][j:=s%n]:
   if len({*(h:=[*zip(*g)][j])})<2:
    o[i][j]=c
    if j<n-1:o[i][j+1]=c*(c in g[i][j+1:])
    if j>0:o[i][j-1]=c*(c in g[i][:j])
   elif len({*g[i]})<2:
    o[i][j]=c
    if i<m-1:o[i+1][j]=c*(c in h[i+1:])
    if i>0:o[i-1][j]=c*(c in h[:i])
 return o