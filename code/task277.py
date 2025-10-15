def p(f,a=range(10)):
 def p(e,i,s):
  if{e,i}-{*a}or s!=f[e][i]^1:return 0
  f[e][i]=s;return-~sum(p(e-1+n//3,i-1+n%3,s)for n in a[:9])
 d={p(e,i,9)for i in a for e in a}-{0};return[[((r:=f[e][i])>2)+(p(e,i,r^1)==min(d))for i in a]for e in a]