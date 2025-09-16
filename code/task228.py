def p(g):
 X=[*map(bool,V:=sum(g,[]))].index(1);J=X%10
 for t,s in(a:=g[I:=X//10].count(x:=V[X]),b:=V[X::10].count(x)),(-1,b),(a,-1),(-1,-1):g[I+s][J+t]=g[A:=I+b+1-s-(s<0)*4][B:=J+a+1-t-(t<0)*4];g[A][B]=0
 return g