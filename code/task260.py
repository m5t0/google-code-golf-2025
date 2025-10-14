c=enumerate
g=lambda n,m:m([o-e for o,z in c(n)for e,p in c(zip(*n))if(z[e-1]==5,p[o-1]==5)[m(0,1)]>p[o]]+[15-30*m(0,1)])
p=lambda n:[[p-5and(p or(o-e)in(g(n,max)+1,g(n,min)-1)and sum({*sum(n,[])})-5)for e,p in c(z)]for o,z in c(n)]