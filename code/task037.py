def p(g,r=range):
 for k in r(1,s:=10):
  a,b=[i for i in r(s*s)if g[i//s][i%s]==k]or[0,0]
  for i in r(b//s-a//s):g[a//s+i][a%s+((a%s<b%s)-(b%s<a%s))*i]=k
 return g