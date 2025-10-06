f=lambda v,j:(s:=len({*v})-1)>1and sum(v[j%s::s])
p=lambda g,e=enumerate:[[f(v,j)or f(w,i)for j,w in e(zip(*g))]for i,v in e(g)]