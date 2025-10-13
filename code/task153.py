t=enumerate
def n(i,e,p,s):
 n=1
 for g,a in t(e):
  for e,r in t(a):
   if r:
    if(a:=p+g)<3>(e:=s+e)and i[a][e]<1:i[a][e]=r
    else:n=0
 return n
def p(e,r=range(16)):
 e,p=[a for g in r[1:]if(a:=[[r[p]for r in zip(*e)if g in r]for p,a in t(e)if g in a])]
 for a in r:
  i=[[0]*3for a in r[:3]]
  if n(i,e,a//8,a//4%2)&n(i,p,a%4//2,a%2):return i