f=lambda g,t=0:[[t|(t:=t^x)for x in v]for v in zip(*g)]
p=lambda g:f(f([[max({*v}&{*w})for w in zip(*g)]for v in g]))