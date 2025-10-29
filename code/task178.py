f=lambda g,t=0:[t:=v for v in zip(*g)if t!=v]
p=lambda g:f(f(g))