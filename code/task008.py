def p(g,e=enumerate):
 h=lambda n:[(i,j)for i,r in e(g)for j,v in e(r)if v==n];a,c=h(2),h(8);u,z=lambda l:[*map(min,*l),*map(max,*l)],lambda t,b,T,B:(b<T)*(T+~b)+(B<t)*(B-t+1);y=u(a)+u(c)
 for i,j in a:g[i][j]=0
 for i,j in a:g[i+z(*y[::2])][j+z(*y[1::2])]=2
 return g