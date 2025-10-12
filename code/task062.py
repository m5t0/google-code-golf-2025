def a(o):
 for r in range(9):
  if{*o[r]}=={0,2}and{*o[r+1]}=={0}:return[[r or 3for r in r]for r in(o[:r]+o[r-1::-1]+[[0]*10]*9)[:10]]
r=lambda o:a(o)or(r:=a(o[::-1]))and r[::-1]
p=lambda o:r(o)or[*zip(*r([*zip(*o)]))]