def p(g,r=range,e=enumerate):
 a,*l,n=sum(g,[]),10
 for i,v in e(g):
  if(5in v)>i/9<(0in v[(x:=v.index(5)+1):(y:=9-v[::-1].index(5))]):l+=[k for j in r(x,y)if a[k:=i*n+j]<1]
  else:[a==exec("a[m-b[0]+l[0]],a[m]=a[m],0")for b in[[i for i,v in e(a)if v==c]for c in r(n)]if[m-b[0]for m in b]==[m-l[0]for m in l]for m in b];l=[]
 return[a[i*n:][:n]for i in r(n)]