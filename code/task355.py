def p(g,r=range):
 d={}
 for k in r(10):
  a=[(i,j)for i in r(len(g))for j in r(len(g[0]))if g[i][j]==k]
  if a:b,c=zip(*a);d[k]=-sum(x!=k for i in r(b[0],b[-1]+1)for x in g[i][min(c):max(c)+1])
 return[[sorted(d,key=d.get)[1]]]