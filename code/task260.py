e=enumerate
f=lambda g,m:m([i-j for i,v in e(g)for j,w in e(zip(*g))if(v[j-1]==5,w[i-1]==5)[m(0,1)]>w[i]]+[15-30*m(0,1)])
p=lambda g:[[w-5and(w or(i-j)in(f(g,max)+1,f(g,min)-1)and sum({*sum(g,[])})-5)for j,w in e(v)]for i,v in e(g)]