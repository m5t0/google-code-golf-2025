def p(m):
 f={};d,i=[],[]
 for a,e in enumerate(m):
  for o,e in enumerate(e):
   if e:f[(a,o)]=e;[d,[]][e-1]+=[(a,o)]
 def p(a,o):
  if(a,o)in f:[d,i][f.pop((a,o))-1]+=[(a,o)];p(a,o+1),p(a,o-1),p(a+1,o),p(a-1,o)
 p(*min(d))
 while f:
  a,o=min(f);n=[n for n in(3,2,1)if[*zip(*m[a:a+n])][o:o+n]==[(2,)*n]*n][0]
  for p,e in d+i:
   for r in range(n):
    for u in range(n):b=a+(p-min(i)[0])*n+r;h=o+(e-min(i)[1])*n+u;m[b][h]=(h>=0)*f.pop((b,h),1)
 return m