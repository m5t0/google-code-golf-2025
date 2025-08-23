def p(g,r=range):
 for I in r(81)[::-1]:
  for k in((x:=g[i:=I//9][j:=I%9])*(y:=g[i+1][j])*(z:=g[i][j+1])>0)*[*r(len({x,y,z,g[i+1][j+1]}))]:g[i+2+k][j]=g[i+2+k][j+1]=3
 return g