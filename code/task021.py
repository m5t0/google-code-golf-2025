f=lambda g,s=0:[s:=v for v in zip(*g)if s!=v][::2]
p=lambda g:f(f(g))