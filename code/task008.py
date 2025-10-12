def p(x,e=enumerate):
 m=lambda n:[(u,i)for u,i in e(x)for i,a in e(i)if a&n];i=lambda n:[*map(min,*n),*map(max,*n)];r=lambda x,r,n,e:max(n-r-1,0)-max(x-e-1,0);n=i(a:=m(2))+i(m(8))
 for u,i in a:x[u][i]=0
 for u,i in a:x[u+r(*n[::2])][i+r(*n[1::2])]=2
 return x