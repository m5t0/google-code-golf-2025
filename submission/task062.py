f=lambda l:next(([[w or 3for w in v]for v in(l[:i]+l[i-1::-1]+[r]*9)[:10]]for i in range(9)if{*l[i]}=={0,2}and sum(r:=l[i+1])<1),[])
h=lambda l:f(l)or f(l[::-1])[::-1]
p=lambda g:h(g)or[*zip(*h([*zip(*g)]))]