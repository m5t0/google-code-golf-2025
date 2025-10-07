def p(g,r=range):
 for I in r(81)[::-1]:
  s={g[i:=I//9+k//2][j:=I%9+k%2]for k in r(4)}
  for k in min(s)*[*r(len(s))]:g[t:=i+1+k][j-1]=g[t][j]=3
 return g