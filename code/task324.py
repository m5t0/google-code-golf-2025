def p(d,r=range):
 c,m,j,l,t=[],len(d[0]),len(d),[d]*5,sum(d,[])
 for s in r(9):c+=[s+1]*(0<t.count(s+1)<3)
 a=o=d[0][d[0][0]in c];x=sum({*t}-{*c,a})
 if any(d[s][q]==c[0]and sum((s==a)-(s==x)for v in d[s and s-1:s+2]for s in v[q and q-1:q+2])>0for s in r(j)for q in r(m)):o=x
 for s in r(4):
  l=[[*map(list,zip(*q))][::-1]for q in l];v=l[s]
  for s in r(len(v)-1):
   for e in r(len(v[0])-1):
    if v[s][e]in c:v[s+1][e+1]=l[4][s+1][e+1]=c[0]
 return[[[l[4][q][s],c[d[q][s]in(o,c[1])]][l[4][q][s]in c]for s in r(m)]for q in r(j)]