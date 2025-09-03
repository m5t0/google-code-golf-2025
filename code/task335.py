def p(g,e=enumerate):
 f=lambda n:[(i,j)for i,v in e(g)for j,w in e(v)if w==n][0];a,b=f(8);c,d=f(2)
 while a-c:a+=(a<c)-(a>c);g[a][b]=4
 while b-d:b+=(b<d)-(b>d);g[a][b]=4;g[c][d]=2
 return g