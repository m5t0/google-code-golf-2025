e=enumerate
f=lambda g,m:m([i-j for i,v in e(g)for j,w in e(zip(*g))if((m==max)*(5in w[i-1:i])>w[i])-((m==min)*(5in v[j-1:j])>w[i])]+[15-30*(m==max)])
p=lambda g:[[w-5and(w or(f(g,max)==i-j-1or f(g,min)==i-j+1)*(sum({*sum(g,[])})-5))for j,w in e(v)]for i,v in e(g)]