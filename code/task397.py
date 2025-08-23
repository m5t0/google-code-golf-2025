def p(g,r=range):
 for I in r(81)[::-1]:
  for k in((x:=g[i:=I//9][j:=I%9])*(y:=g[i+1][j])*(z:=g[i][s:=j+1]))*[*r(len({x,y,z,g[i+1][s]}))]:g[t:=i+2+k][j]=g[t][s]=3
 return g