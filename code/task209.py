def p(e):
 r=lambda l,m:m(o for o,f in enumerate(l)if 4in f);o,g,p,l=r(e,min),r(e,max),r(zip(*e),min),r(zip(*e),max);r=[f[p:l+1]for f in e[o:g+1]];e=[[o for*f,o in zip(*e[g+1:],f)if any(f)]for f in e[g+1:]if any(f)]
 for f in 2,3,4:
  for o in range(len(r)):
   for g in range(len(r[0])):
    if all(r[p][l]in{0,4}or len(e)*f>p-o>-1<l-g<len(e[0])*f and r[p][l]==e[(p-o)//f][(l-g)//f]for p in range(len(r))for l in range(len(r[0]))):
     for p in range(len(r)):
      for l in range(len(r[0])):
       if len(e)*f>p-o>-1<l-g<len(e[0])*f:r[p][l]=e[(p-o)//f][(l-g)//f]
     return r