def p(g):
 a=[[w for w in v if w%5]for v in g if{*v}-{0,5}]
 while 5in(v:=sum(g,[])):
  for V,A in zip(g[(X:=v.index(5))//10:],a):V[X%10:X%10+len(A)]=A
 return g