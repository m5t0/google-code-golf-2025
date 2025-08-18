# for文を使う実装
def p(g,e=enumerate):
 h=lambda n:[(i,j)for i,r in e(g)for j,v in e(r)if v==n];a,c=h(2),h(8);u,z=lambda l:[*map(min,zip(*l)),*map(max,zip(*l))],lambda t,b,T,B:(b<T)*(T-b-1)+(B<t)*(B-t+1);y=u(a)+u(c);
 for i,j in a:g[i][j]=0
 for i,j in a:g[i+z(*y[::2])][j+z(*y[1::2])]=2
 return g

# 少し短くした実装
def p(g,e=enumerate):h=lambda n:[(i,j)for i,r in e(g)for j,v in e(r)if v==n];a,c=h(2),h(8);u,z=lambda l:[*map(min,zip(*l)),*map(max,zip(*l))],lambda t,b,T,B:(b<T)*(T-b-1)+(B<t)*(B-t+1);y=u(a)+u(c);return[[2*((i-z(*y[::2]),j-z(*y[1::2]))in a)+8*((i,j)in c)for j,w in e(v)]for i,v in e(g)]

# 変数をたくさん使って実装
def p(g,e=enumerate):h=lambda n:[(i,j)for i,r in e(g)for j,v in e(r)if v==n];a,c=h(2),h(8);u=lambda l:[*map(min,zip(*l)),*map(max,zip(*l))];t,l,b,r,T,L,B,R=u(a)+u(c);return[[2*((i-(b<T)*(T-b-1)-(B<t)*(B-t+1),j-(r<L)*(L-r-1)-(R<l)*(R-l+1))in a)+8*((i,j)in c)for j,w in e(v)]for i,v in e(g)]

def p(g, e=enumerate):
    h = lambda n: [(i, j) for i, r in e(g) for j, v in e(r) if v == n]
    a, c = h(2), h(8)
    u, z = (
        lambda l: [*map(min, zip(*l)), *map(max, zip(*l))],
        lambda t, b, T, B: (b < T) * (T - b - 1) + (B < t) * (B - t + 1),
    )
    y = u(a) + u(c)
    for i,j in a:g[i][j]=0;g[i+z(*y[::2])][j+z(*y[1::2])]=2
    return g
