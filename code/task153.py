e=enumerate
def n(m,s,i,l):
 n=1
 for a,z in e(s):
  for j,t in e(z):
   if t:
    if(z:=i+a)<3>(s:=l+j)and m[z][s]<1:m[z][s]=t
    else:n=0
 return n
def p(j,t=range(16)):
 s,i=[z for a in t[1:]if(z:=[[t[i]for t in zip(*j)if a in t]for i,z in e(j)if a in z])]
 for o in t:
  m=[[0]*3for o in t[:3]]
  if n(m,s,o//8,o//4%2)&n(m,i,o%4//2,o%2):return m