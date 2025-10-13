def p(f,e=enumerate):
 a,t=[(i,o,t)for i,r in e(f)for o,t in e(r)if t]
 for e,l,n in a,t:
  while abs((i:=a[0]+t[0]-2*e)+(o:=a[1]+t[1]-2*l))>2:f[e][l]=n;e+=(i>0)-(i<0);l+=(o>0)-(o<0)
  for x in-2,-1,1,2:f[e-i+x*o][l-o+x*i]=f[e+2*o][l+2*i]=f[e-2*o][l-2*i]=n
 return f