def p(g):
 f=lambda n:divmod(sum(g,[]).index(n),len(g[0]));a,b=f(3);c,d=f(2)
 while a-c:a+=(a<c)-(a>c);g[a][b]=8
 while b-d:g[a][b]=8;b+=(b<d)-(b>d)
 return g