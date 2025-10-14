def p(e,p=range,i=enumerate):
 f,*n,m=sum(e,[]),10
 for d,r in i(e):
  if(5in r)>d/9<(0in r[(e:=r.index(5)+1):(r:=9-r[::-1].index(5))]):n+=[n for i in p(e,r)if f[n:=d*m+i]<1]
  else:[f==exec("f[m-i[0]+n[0]],f[m]=f[m],0")for i in[[d for d,r in i(f)if r==m]for m in p(m)]if[m-i[0]for m in i]==[m-n[0]for m in n]for m in i];n=[]
 return[f[d*m:][:m]for d in p(m)]