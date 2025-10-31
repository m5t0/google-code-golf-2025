f=lambda l:[0]+[i+1for i,v in enumerate(l)if any(v)^1]
p=lambda g:[[max(g[i+1][k:k+4])for k in f(zip(*g))]for i in f(g)]