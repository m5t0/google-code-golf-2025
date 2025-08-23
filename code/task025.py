def p(g,r=range):
 g=[[*zip(*g)],g][v:=any(len({*[*zip(*g)][j]})<2for j in r(len(g[0])))];m,n=len(g),len(g[0]);o=[n*[0]for _ in r(m)]
 for s in r(m*n):
  if(c:=g[i:=s//n][j:=s%n])*(len({*([*zip(*g)][j])})<2):
   o[i][j]=c
   if j<n-1:o[i][j+1]=c*(c in g[i][j+1:])
   if j:o[i][j-1]=c*(c in g[i][:j])
 return [[[*[*zip(*o)][j]]for j in r(n)],o][v]