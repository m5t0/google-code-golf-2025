def p(g,e=enumerate,r=range):
 d={}
 for k in r(10):
  if a:=[(i,j)for i,v in e(g)for j,w in e(v)if w==k]:b,c=zip(*a);d[k]=-sum(x!=k for i in r(b[0],b[-1]+1)for x in g[i][min(c):max(c)+1])
 return[[sorted(d,key=d.get)[1]]]