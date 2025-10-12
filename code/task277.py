def p(t,f=range(10)):
 def p(c,g,r):
  if{c,g}-{*f}or r!=t[c][g]^1:return 0
  t[c][g]=r;return-~sum(p(c-1+a//3,g-1+a%3,r)for a in f[:9])
 e={p(c,g,9)for g in f for c in f}-{0};return[[((i:=t[c][g])>2)+(p(c,g,i^1)==min(e))for g in f]for c in f]