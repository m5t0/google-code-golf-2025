f=lambda g:[*filter(any,zip(*g))]
p=lambda g:[v[:3]for v in f(f(g))[:3]]