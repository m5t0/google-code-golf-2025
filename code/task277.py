def p(i,r=range(10)):
 def p(_,u,t):
  if{_,u}-{*r}or t!=i[_][u]^1:return 0
  i[_][u]=t;return-~sum(p(_-1+f//3,u-1+f%3,t)for f in r[:9])
 d={p(_,u,9)for u in r for _ in r}-{0};return[[((f:=i[_][u])>2)+(p(_,u,f^1)==min(d))for u in r]for _ in r]