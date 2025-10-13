def p(d,e=range):
 f=0;n=len(d)
 for a in e(n):
  if len(i:=[a for a,l in enumerate(d[a])if l%5])==2:
   q,i=i
   for l in e(9):
    if l-4:d[a+l//3-1][q+l%3-1]=d[a][i];d[a+l//3-1][i+l%3-1]=d[a][q]
   for l in e(1,i-q):
    if min(l,i-q-l)%2==0:d[a][q+l]=5
   if f<1:
    for l in e(1,f:=(r:=[a for a in e(n)if d[a][q]%5])[3]-r[1]):
     if min(l,f-l)%2==0:d[r[1]+l][q]=d[r[1]+l][i]=5
 return d