def p(k,d=range):
 f,e=len(k),len(k[0]);l,*o=[],
 for j in d(f*e):
  if k[m:=j//e][p:=j%e]==2:
   l+=(c:={(0,0)}),;o+=(m,p),
   for j in d(50):c|={(h,q)for l,n in c for j in d(9)if e>p+(q:=n+j%3-1)>=0<f>m+(h:=l+j//3-1)>=0<k[m+h][p+q]}
 n,p=o[l.index(c:=max(l,key=len))];r=c
 for i,(m,f)in zip(l,o):
  for j in d(-3,5):
   if i<{*c}and all(((l,j)in i)<=(k[m+l][f+j]==k[n+h][p+q])for(l,j),(h,q)in zip(c,r)):
    for(l,j),(h,q)in zip(c,r):k[m+l][f+j]=k[n+h][p+q]
   c=[(-j,l)for l,j in c];j or(c:=[(-l,j)for l,j in c])
 return k