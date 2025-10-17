f=lambda g,t=0:[[t|(t:=t^max({*v}&{*w}))for w in g]for v in zip(*g)]
p=lambda g:f(f(g))