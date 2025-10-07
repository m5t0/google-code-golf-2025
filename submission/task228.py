def p(g):
 I,J=divmod(X:=[*map(bool,V:=sum(g,[]))].index(1),10);a=g[I].count(x:=V[X]);b=V[X::10].count(x)
 for t,s in(a,b),(-1,b),(a,-1),(-1,-1):g[I+s][J+t]=g[A:=I+b+1-s-(s<0)*4][B:=J+a+1-t-(t<0)*4];g[A][B]=0
 return g