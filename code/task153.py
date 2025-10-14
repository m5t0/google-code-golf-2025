r=enumerate
def g(i,n,s,f):
 g=1
 for a,e in r(n):
  for n,z in r(e):
   if z:
    if(e:=s+a)<3>(n:=f+n)and i[e][n]<1:i[e][n]=z
    else:g=0
 return g
def p(n,z=range(16)):
 n,s=[e for a in z[1:]if(e:=[[z[s]for z in zip(*n)if a in z]for s,e in r(n)if a in e])]
 for e in z:
  i=[[0]*3for e in z[:3]]
  if g(i,n,e//8,e//4%2)&g(i,s,e%4//2,e%2):return i