f=lambda g:[max([*zip(*g)][i%10::10])for i in range(len(g[0]))]
p=lambda g:f(f(g))