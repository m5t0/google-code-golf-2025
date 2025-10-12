def p(d,e=enumerate):
 f=lambda n:[(i,b)for i,r in e(d)for b,f in e(r)if f&n];u=lambda i:[*map(min,*i),*map(max,*i)];r=lambda r,b,u,n:max(u-b-1,0)-max(r-n-1,0);e=u(a:=f(2))+u(f(8))
 for i,b in a:d[i][b]=0
 for i,b in a:d[i+r(*e[::2])][b+r(*e[1::2])]=2
 return d