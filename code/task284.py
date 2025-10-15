def p(h,u=enumerate):
 l,u=[(r,t,s)for r,e in u(h)for t,s in u(e)if s]
 for e,a,s in l,u:
  while abs((r:=l[0]+u[0]-2*e)+(t:=l[1]+u[1]-2*a))>2:h[e][a]=s;e+=(r>0)-(r<0);a+=(t>0)-(t<0)
  for f in-2,-1,1,2:h[e-r+f*t][a-t+f*r]=h[e+2*t][a+2*r]=h[e-2*t][a-2*r]=s
 return h