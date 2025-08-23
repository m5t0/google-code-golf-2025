def p(g):
 r,m,n=range,len(g),len(g[0]);o=[n*[0]for _ in r(m)]
 for s in r(m*n):
  if(c:=g[i:=s//n][j:=s%n])*(len({*(h:=[*zip(*g)][j])})<2):
   o[i][j]=c
   if j<n-1:o[i][j+1]=c*(c in g[i][j+1:])
   if j:o[i][j-1]=c*(c in g[i][:j])
  if(len({*g[i]})<2)*c:
   o[i][j]=c
   if i<m-1:o[i+1][j]=c*(c in h[i+1:])
   if i:o[i-1][j]=c*(c in h[:i])
 return o