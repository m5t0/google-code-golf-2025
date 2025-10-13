def p(n,e=enumerate):
 m=lambda m:[(d,i)for d,i in e(n)for i,a in e(i)if a&m];i=lambda m:[*map(min,*m),*map(max,*m)];r=lambda n,r,m,e:max(m-r-1,0)-max(n-e-1,0);m=i(a:=m(2))+i(m(8))
 for d,i in a:n[d][i]=0
 for d,i in a:n[d+r(*m[::2])][i+r(*m[1::2])]=2
 return n