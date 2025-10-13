f=enumerate
l=lambda n,m:m([d-a for d,z in f(n)for a,i in f(zip(*n))if(z[a-1]==5,i[d-1]==5)[m(0,1)]>i[d]]+[15-30*m(0,1)])
p=lambda n:[[i-5and(i or(d-a)in(l(n,max)+1,l(n,min)-1)and sum({*sum(n,[])})-5)for a,i in f(z)]for d,z in f(n)]