def f(l,b=1):
 for i in range(9):
  if{*l[i]}=={0,2}and{*l[i+1]}=={0}:return[[[3,w][w>0]for w in v]for v in(l[:i]+l[:i][::-1]+[[0]*10]*9)[:10]]
 if b and(v:=f(l[::-1],0)):return v[::-1]
p=lambda g:f(g)or[*map(list,zip(*f([*zip(*g)])))]