def p(g,e=enumerate):
 h=lambda n:[(i,j)for i,r in e(g)for j,v in e(r)if v&n];u=lambda l:[*map(min,*l),*map(max,*l)];z=lambda t,b,T,B:max(T-b-1,0)-max(t-B-1,0);y=u(a:=h(2))+u(h(8))
 for i,j in a:g[i][j]=0
 for i,j in a:g[i+z(*y[::2])][j+z(*y[1::2])]=2
 return g