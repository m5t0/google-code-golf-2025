f=lambda g:[*filter(any,zip(*g))]
def p(g):h=f(f(g[::3])[::3]);return[[c&d for c in a for d in b]for a in h for b in h]