p=lambda g:[[w[g.index(v)]for w in zip(*g)if len({*w})>2]for v in g if len({*v})>2]

f=lambda g:filter(lambda v:len({*v})>2,g)
p=lambda g:[[w[g.index(v)]for w in[*f(zip(*g))]]for v in[*f(g)]]