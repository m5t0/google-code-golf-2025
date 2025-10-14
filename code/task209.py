def p(n):
 r=lambda r,n:n(m for m,e in enumerate(r)if 4in e);m,d,h,r=r(n,min),r(n,max),r(zip(*n),min),r(zip(*n),max);a=[e[h:r+1]for e in n[m:d+1]];n=[[m for*e,m in zip(*n[d+1:],e)if any(e)]for e in n[d+1:]if any(e)]
 for e in 2,3,4:
  for m in range(len(a)):
   for d in range(len(a[0])):
    if all(a[h][r]in{0,4}or len(n)*e>h-m>-1<r-d<len(n[0])*e and a[h][r]==n[(h-m)//e][(r-d)//e]for h in range(len(a))for r in range(len(a[0]))):
     for h in range(len(a)):
      for r in range(len(a[0])):
       if len(n)*e>h-m>-1<r-d<len(n[0])*e:a[h][r]=n[(h-m)//e][(r-d)//e]
     return a