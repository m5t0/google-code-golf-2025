f=lambda g:[v for v in zip(*g)for _ in"__"*any(v)]
p=lambda g:f(f(g))