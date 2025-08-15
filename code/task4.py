def p(g):
 v=[0]*10
 for a in g[::-1]:
  for i in range(len(a))[::-1]:
    x,y=a[i],a[i - 1];v[x]=max(v[x],i)
    if i>0 and i<=v[y] and y>0:a[i],a[i - 1]=y,x
 return g