f=lambda g,x=0:[x:=b for b in zip(*g)if x!=b]
p=lambda g:f(f(g))