def p(n,h=range(10)):
 def p(g,s,m):
  if{g,s}-{*h}or m!=n[g][s]^1:return 0
  n[g][s]=m;return-~sum(p(g-1+f//3,s-1+f%3,m)for f in h[:9])
 t={p(g,s,9)for s in h for g in h}-{0};return[[((o:=n[g][s])>2)+(p(g,s,o^1)==min(t))for s in h]for g in h]