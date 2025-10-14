def p(e,f=range(10)):
 def p(g,a,r):
  if{g,a}-{*f}or r!=e[g][a]^1:return 0
  e[g][a]=r;return-~sum(p(g-1+u//3,a-1+u%3,r)for u in f[:9])
 n={p(g,a,9)for a in f for g in f}-{0};return[[((i:=e[g][a])>2)+(p(g,a,i^1)==min(n))for a in f]for g in f]