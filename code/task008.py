def p(t,p=enumerate):
 f=lambda i:[(m,n)for m,r in p(t)for n,f in p(r)if f&i];m=lambda m:[*map(min,*m),*map(max,*m)];r=lambda r,n,m,i:max(m-n-1,0)-max(r-i-1,0);p=m(i:=f(2))+m(f(8))
 for m,n in i:t[m][n]=0
 for m,n in i:t[m+r(*p[::2])][n+r(*p[1::2])]=2
 return t