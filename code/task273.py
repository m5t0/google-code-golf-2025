def p(g):
 r=range(10);d={}
 for i in r:
  a=b=0
  for j in r:g[i][j]&4and(a:=b,b:=j)
  for x in g[d.get((a,b),i)+1:i]:x[a+1:b]=[2]*(b+~a)
  d[a,b]=i
 return g