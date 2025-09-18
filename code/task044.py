def p(g,r=range,e=enumerate):
 a,*l=sum(g,[]),;n=10;s=[h for c in r(1,n)if c!=5if(h:=[i for i in r(100)if a[i]==c])if all((a[i-(i>0):i+2]+a[i-n*(i>9):i+11:n]).count(c)>2for i in h)]
 for i,v in e(g):
  if(5in v)>i/9and 0in{*v[(x:=(o:=str(v)[1::3]).find("5")+1):(y:=o.rfind("5"))]}:l+=[j for j in r(i*n+x,i*n+y)if a[j]<1]
  elif l:
   for b in s:
    if len(b)==len(l)and all(k-b[0]==l[m]-l[0]for m,k in e(b)):
     for m in b:a[m-b[0]+l[0]]=a[m];a[m]=0
   l=[]
 return[a[i*n:][:n]for i in r(n)]