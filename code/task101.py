def p(e):
 Y={};p,c=[],[]
 for f,_ in enumerate(e):
  for n,o in enumerate(_):
   if o:Y[(f,n)]=o;[p,[]][o-1]+=[(f,n)]
 def w(f,n):
  if(f,n)in Y:[p,c][Y.pop((f,n))-1]+=[(f,n)];w(f,n+1),w(f,n-1),w(f+1,n),w(f-1,n)
 w(*min(p))
 while Y:
  f,n=min(Y);i=[i for i in(3,2,1)if[*zip(*e[f:f+i])][n:n+i]==[(2,)*i]*i][0]
  for a,o in p+c:
   for x in range(i):
    for s in range(i):h=f+(a-min(c)[0])*i+x;g=n+(o-min(c)[1])*i+s;e[h][g]=(g>=0)*Y.pop((h,g),1)
 return e