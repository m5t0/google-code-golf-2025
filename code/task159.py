def p(g,r=range):
 n=sum(2in v for v in g)-2;m=n//3;a=[[2]*(n+2)]
 for c in r(10):
  if len(l:=[[x for x,w in zip(v,zip(*g))if c in w]for v in g if c in v])==3:return a+[[2,*(l[i//m][j//m]for j in r(n)),2]for i in r(n)]+a