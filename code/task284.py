def p(h,s=enumerate):
 t,s=[(u,f,e)for u,r in s(h)for f,e in s(r)if e]
 for r,l,e in t,s:
  while abs((u:=t[0]+s[0]-2*r)+(f:=t[1]+s[1]-2*l))>2:h[r][l]=e;r+=(u>0)-(u<0);l+=(f>0)-(f<0)
  for a in-2,-1,1,2:h[r-u+a*f][l-f+a*u]=h[r+2*f][l+2*u]=h[r-2*f][l-2*u]=e
 return h