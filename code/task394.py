def p(g,r=range):
 for I in r((s:=len(g))*s):
  if g[i:=I//s][I%s]<1:x=g[i].count(0);return[[[y:=g[t:=(i+k)%(z:=2+(s>6))][w:=(I%s+l)%z],g[t+z][w]][y<1]for l in r(x)]for k in r(x)]