def p(g,r=range):
 def f(k):
  for i in r(a[0],a[-1]+1):g[i][k]=t
 for j in r(10):
  a=[i for i in r(10)if g[i][j]==5]
  if t:=g[0][j]:
   f(j)
   for l in(-1,1):
    for k in r(1,10):
     if-1<(s:=j+k*l)<10and g[a[0]][s]==5:f(s)
     else:break
 return g