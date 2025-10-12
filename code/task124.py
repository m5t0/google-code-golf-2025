def p(o,z=range):
 f,d=len(o),len(o[0])
 for u in z(1,10):
  l,i=u//3,u%3
  if all((o[u]<1)^(f[u+i]>0)for o,f in zip(o,o[l:])for u in z(d-i)):
   o=[o+[0]*(10-d)for o in o]+[[0]*10for u in z(10-f)]
   for u in z(100):o[d][u]=o[d:=u//10][u:=u%10]or(d-l>-1<u-i)*o[d-l][u-i]
   return o