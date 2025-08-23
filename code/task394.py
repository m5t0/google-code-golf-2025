def p(g,r=range):
 for I in r((s:=len(g))*s):
  if g[i:=I//s][j:=I%s]<1:x=g[i].count(0);return[[[y:=g[(i+k)%(z:=2+(s>6))][(j+l)%z],g[(i+k)%z+z][(j+l)%z]][y<1]for l in r(x)]for k in r(x)]