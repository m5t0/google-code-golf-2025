def p(j):
 r=lambda h,f:f(m for m,d in enumerate(h)if 4in d);m,n,c,r=r(j,min),r(j,max),r(zip(*j),min),r(zip(*j),max);a=[d[c:r+1]for d in j[m:n+1]];f=[[m for*d,m in zip(*j[n+1:],d)if any(d)]for d in j[n+1:]if any(d)]
 for d in 2,3,4:
  for m in range(len(a)):
   for n in range(len(a[0])):
    if all(a[c][r]in{0,4}or len(f)*d>c-m>-1<r-n<len(f[0])*d and a[c][r]==f[(c-m)//d][(r-n)//d]for c in range(len(a))for r in range(len(a[0]))):
     for c in range(len(a)):
      for r in range(len(a[0])):
       if len(f)*d>c-m>-1<r-n<len(f[0])*d:a[c][r]=f[(c-m)//d][(r-n)//d]
     return a