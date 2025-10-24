f=lambda g,s=0:[v for v in zip(*g)if s|(s:=s^all(v))]
h=lambda g:[[max({w}|{v[0]}&{*v[j:]}|{v[-1]}&{*v[:j]})for j,w in enumerate(v)]for v in zip(*g)]
p=lambda g:h(h(f(f(g))))