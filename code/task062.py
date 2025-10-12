def t(p):
 for r in range(9):
  if{*p[r]}=={0,2}and{*p[r+1]}=={0}:return[[r or 3for r in r]for r in(p[:r]+p[r-1::-1]+[[0]*10]*9)[:10]]
r=lambda p:t(p)or(r:=t(p[::-1]))and r[::-1]
p=lambda p:r(p)or[*zip(*r([*zip(*p)]))]