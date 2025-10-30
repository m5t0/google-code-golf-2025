def p(t,i=enumerate):
 m,i=[(e,r,d)for e,n in i(t)for r,d in i(n)if d]
 for n,f,d in m,i:
  while 2<abs((e:=m[0]+i[0]-2*n)+(r:=m[1]+i[1]-2*f)):t[n][f]=d;n+=(0<e)-(e<0);f+=(0<r)-(r<0)
  for a in-2,-1,1,2:t[n-e+a*r][f-r+a*e]=t[n+2*r][f+2*e]=t[n-2*r][f-2*e]=d
 return t