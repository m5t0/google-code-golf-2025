def p(g,s=range(-2,10)):
 for i in s:
  for j in s:
   for a in((n:=g[i+1][j])==g[i-1][j]==g[i][j+1]>0)*[*s[:5]]:c=g[i][j];g[i-a][j]=g[i][j-a]=n;g[i+a][j+a]=g[i+a][j-a]=c
 return g


def p(g,r=range(2,10)):
 for i,j in((i,j)for j in r for i in r if(c:=g[i][j])==min(v:=sum(g,[]),key=v.count)):
  for a in[-2,-1,1,2]:n=g[i+1][j];g[i+a][j]=g[i][j+a]=n;g[i+a][j+a]=g[i+a][j-a]=c
 return g