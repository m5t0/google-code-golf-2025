def p(g):
 v=[0]*10
 for a in g[::-1]:
  for i in range(len(a))[::-1]:
   v[x]=max(v[x:=a[i]],i)
   if v[y:=a[i-1]]>=i>0<y:a[i],a[i-1]=y,x
 return g