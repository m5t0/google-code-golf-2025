def p(g):
 f=lambda n:divmod(sum(g,[]).index(n),len(g[0]));a,b=f(8);c,d=f(2)
 while a-c:g[a:=a+(a<c or-1)][b]=4
 while b-d:g[a][b]=4;b+=b<d or-1
 return g