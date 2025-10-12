def p(o,r=range):
 f,n=len(o),len(o[0])
 for u in r(1,10):
  l,t=u//3,u%3
  if all((i[u]<1)^(f[u+t]>0)for i,f in zip(o,o[l:])for u in r(n-t)):
   i=[i+[0]*(10-n)for i in o]+[[0]*10for u in r(10-f)]
   for u in r(100):i[d][u]=i[d:=u//10][u:=u%10]or(d-l>-1<u-t)*i[d-l][u-t]
   return i