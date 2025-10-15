def p(a):
 n=lambda n,a:a(d for d,e in enumerate(n)if 4in e);d,f,i,n=n(a,min),n(a,max),n(zip(*a),min),n(zip(*a),max);l=[e[i:n+1]for e in a[d:f+1]];a=[[d for*e,d in zip(*a[f+1:],e)if any(e)]for e in a[f+1:]if any(e)]
 for e in 2,3,4:
  for d in range(len(l)):
   for f in range(len(l[0])):
    if all(l[i][n]in{0,4}or len(a)*e>i-d>-1<n-f<len(a[0])*e and l[i][n]==a[(i-d)//e][(n-f)//e]for i in range(len(l))for n in range(len(l[0]))):
     for i in range(len(l)):
      for n in range(len(l[0])):
       if len(a)*e>i-d>-1<n-f<len(a[0])*e:l[i][n]=a[(i-d)//e][(n-f)//e]
     return l