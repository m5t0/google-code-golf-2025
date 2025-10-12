def p(d,p=range):
 c,m,u,l,t=[],len(d[0]),len(d),[d]*5,sum(d,[])
 for s in p(9):c+=[s+1]*(0<t.count(s+1)<3)
 a=a=d[0][d[0][0]in c];q=sum({*t}-{*c,a})
 if any(d[s][f]==c[0]and sum((s==a)-(s==q)for v in d[s and s-1:s+2]for s in v[f and f-1:f+2])>0for s in p(u)for f in p(m)):a=q
 for s in p(4):
  l=[[*map(list,zip(*f))][::-1]for f in l];v=l[s]
  for s in p(len(v)-1):
   for f in p(len(v[0])-1):
    if v[s][f]in c:v[s+1][f+1]=l[4][s+1][f+1]=c[0]
 return[[[l[4][f][s],c[d[f][s]in(a,c[1])]][l[4][f][s]in c]for s in p(m)]for f in p(u)]