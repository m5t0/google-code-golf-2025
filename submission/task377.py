f=lambda g:[*zip(*g[:1]+[b for a,b in zip(g,g[1:])if a!=b])]
p=lambda g:f(f(g))