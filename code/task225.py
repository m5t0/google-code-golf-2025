def p(g):
 I,J=divmod([*map(bool,sum(g,[]))].index(1),6)
 for m in range(16):
  if-1<(a:=I+2-m//8*4+m%4//2)<6>(b:=J+2-(m&4)+m%2)>=0:g[a][b]=g[I+m//8][J+(m&4>0)]
 return g