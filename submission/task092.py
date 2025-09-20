f=lambda w,i:((b:=max(w[:i+1]))==max(w[i:]))*b
p=lambda g,e=enumerate:[[v[j]or f(w,i)or f(v,j)for j,w in e(zip(*g))]for i,v in e(g)]