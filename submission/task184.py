f=lambda l:[-1]+[i for i,v in enumerate(l)if any(v)^1]
p=lambda g:[[max(g[i+2][k+1:k+5])for k in f(zip(*g))]for i in f(g)]
