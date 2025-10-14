def p(k,r=range):
 f,b=len(k),len(k[0]);l,*o=[],
 for j in r(f*b):
  if k[m:=j//b][g:=j%b]==2:
   l+=(c:={(0,0)}),;o+=(m,g),
   for j in r(50):c|={(a,q)for l,n in c for j in r(9)if b>g+(q:=n+j%3-1)>=0<f>m+(a:=l+j//3-1)>=0<k[m+a][g+q]}
 n,g=o[l.index(c:=max(l,key=len))];t=c
 for h,(m,f)in zip(l,o):
  for j in r(-3,5):
   if h<{*c}and all(((l,j)in h)<=(k[m+l][f+j]==k[n+a][g+q])for(l,j),(a,q)in zip(c,t)):
    for(l,j),(a,q)in zip(c,t):k[m+l][f+j]=k[n+a][g+q]
   c=[(-j,l)for l,j in c];j or(c:=[(-l,j)for l,j in c])
 return k