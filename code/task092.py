f=lambda g:[[w or sum({*v[:j]}&{*v[j:]})for j,w in enumerate(v)]for v in zip(*g)]
p=lambda g:f(f(g))