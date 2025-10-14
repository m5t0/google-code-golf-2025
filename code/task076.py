def p(t,h=range):
 m,o=len(t),len(t[0]);i,*n=[],
 for r in h(m*o):
  if t[s:=r//o][f:=r%o]==2:
   i+=(z:={(0,0)}),;n+=(s,f),
   for r in h(50):z|={(u,_)for i,r in z for e in h(9)if o>f+(_:=r+e%3-1)>=0<m>s+(u:=i+e//3-1)>=0<t[s+u][f+_]}
 m,f=n[i.index(z:=max(i,key=len))];p=z
 for k,(s,i)in zip(i,n):
  for r in h(-3,5):
   if k<{*z}and all(((o,e)in k)<=(t[s+o][i+e]==t[m+u][f+_])for(o,e),(u,_)in zip(z,p)):
    for(o,e),(u,_)in zip(z,p):t[s+o][i+e]=t[m+u][f+_]
   z=[(-e,o)for o,e in z];r or(z:=[(-o,e)for o,e in z])
 return t