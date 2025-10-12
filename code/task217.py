f=lambda g:filter(any,zip(*g))
p=lambda g:[[c&d for c in a for d in b]for a in f(f(g))for b in f(f(g))]