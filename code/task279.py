def n(r,e,u,f):
 if len(r)>e>-1<u<len(a:=r[e]):
  if a[u]%9:a[u]^=1;l=max(n(r,e+l//3,~-u+l%3,l)or 0for l in[-2,0,2,4]if l+f-2);a[u]^=1;return l
  return(a[u]<9)*7
p=lambda r,u=enumerate:[[n(r,e,u,1)+a[u]for u,l in u(a)]for e,a in u(r)]