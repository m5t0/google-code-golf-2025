f=lambda g:[[w or(1in{*v[:j]}&{*v[j:]})*8for j,w in enumerate(v)]for v in zip(*g)]
p=lambda g:f(f(g))