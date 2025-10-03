def p(g,r=range):
 n=len(g)
 for _ in r(4):
  for i in r(n):
   for j in r(n-1):
    if(g[i][j]==2)&(g[i][j+1]<1):
     for l in r(6):
      if g[i][j-l-1]<3:s=l;break
     g[i][j:]=[2]*(n-j)
     for l in r(s):g[i-l-1][j:]=[3]*(n-j);g[i+l+1][j:]=[3]*(n-j)
  g=[*map(list,zip(*g))][::-1]
 return g