def p(l,r=range):
 n,f=len(l),len(l[0])
 for o in r(1,10):
  e,i=o//3,o%3
  if all((n[o]<1)^(l[o+i]>0)for n,l in zip(l,l[e:])for o in r(f-i)):
   n=[n+[0]*(10-f)for n in l]+[[0]*10for l in r(10-n)]
   for o in r(100):n[f][o]=n[f:=o//10][o:=o%10]or(f-e>-1<o-i)*n[f-e][o-i]
   return n