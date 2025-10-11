def p(g,d=divmod):
 for _  in[0]*4:v=sum(g,[]);I,J=d(v.index(m:=max({*v}-{0},key=v.count))-11,10);A,B=d(88-v[::-1].index(m),10);g[I][J]=g[A][B];g[A][B]=0;g=[*map(list,zip(*g))][::-1]
 return g