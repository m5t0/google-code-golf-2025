def p(g,r=range):
 n=len(g)
 for _ in r(4):
  for i in r(n):
   for j in r(n-1):
    if g[i][j]==2>g[i][j+1]+1:
     t=n-j;g[i][j:]=t*[2];s=0
     while 2<g[i][j+~s]:s+=1
     for s in r(s):g[i+~s][j:]=g[i-~s][j:]=t*[3]
  g=[*map(list,zip(*g))][::-1]
 return g