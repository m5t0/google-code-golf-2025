f=lambda g:[[w or(s:=len({*v})-1)>1and sum(v[j%s::s])for j,w in enumerate(v)]for v in zip(*g)]
p=lambda g:f(f(g))