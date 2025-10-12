def p(g):
 f=lambda h,m:m(i for i,v in enumerate(h)if 4in v);i,j,k,l=f(g,min),f(g,max),f(zip(*g),min),f(zip(*g),max);a=[v[k:l+1]for v in g[i:j+1]];b=[[x for*w,x in zip(*g[j+1:],v)if any(w)]for v in g[j+1:]if any(v)]
 for d in 2,3,4:
  for i in range(len(a)):
   for j in range(len(a[0])):
    if all(a[k][l]in{0,4}or len(b)*d>k-i>-1<l-j<len(b[0])*d and a[k][l]==b[(k-i)//d][(l-j)//d]for k in range(len(a))for l in range(len(a[0]))):
     for k in range(len(a)):
      for l in range(len(a[0])):
       if len(b)*d>k-i>-1<l-j<len(b[0])*d:a[k][l]=b[(k-i)//d][(l-j)//d]
     return a