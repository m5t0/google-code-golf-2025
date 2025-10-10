def p(a,e=enumerate):
 f=sum(a,[]);p=sum({*f})-8
 for o in f:
  for o,m in e(a):
   for n,f in e(m):
    for n,u in(o-1,n),(o+1,n),(o,n-1),(o,n+1):
     if a[n:n+1]and a[n][u:u+1]==[0]and f&7:a[n][u]=p-f
 return a
