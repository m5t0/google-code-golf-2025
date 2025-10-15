def p(m,n=range):
 d=0;r=len(m)
 for f in n(r):
  if len(e:=[f for f,l in enumerate(m[f])if l%5])==2:
   p,e=e
   for l in n(9):
    if l-4:m[f+l//3-1][p+l%3-1]=m[f][e];m[f+l//3-1][e+l%3-1]=m[f][p]
   for l in n(1,e-p):
    if min(l,e-p-l)%2==0:m[f][p+l]=5
   if d<1:
    for l in n(1,d:=(o:=[f for f in n(r)if m[f][p]%5])[3]-o[1]):
     if min(l,d-l)%2==0:m[o[1]+l][p]=m[o[1]+l][e]=5
 return m