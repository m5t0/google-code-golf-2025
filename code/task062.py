def f(l):
 for i in range(9):
  if{*l[i]}=={0,2}and{*l[i+1]}=={0}:return[[w or 3for w in v]for v in(l[:i]+l[i-1::-1]+[[0]*10]*9)[:10]]
h=lambda l:f(l)or(v:=f(l[::-1]))and v[::-1]
p=lambda g:h(g)or[*zip(*h([*zip(*g)]))]