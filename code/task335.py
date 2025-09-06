def p(g):
 f=lambda n:[(g.index(v),v.index(w))for v in g for w in v if w==n][0];a,b=f(8);c,d=f(2)
 while a-c:a+=(a<c)-(a>c);g[a][b]=4
 while b-d:b+=(b<d)-(b>d);g[a][b]=4
 g[c][d]=2;return g