f=lambda d:[*zip(*[b for a,b in zip([0]+d,d)if a!=b])]
p=lambda g:f(f(g))