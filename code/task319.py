def p(k):
 n=sum(k,[]);e=max(n,key=n.count);z=sorted({*n}-{e})
 for c in z:
  r=[[[e,m][m==c]for*n,m in zip(*k,n)if c in n]for n in k if c in n];d=[[m for m in r for y in'00']for r in r for y in'00']
  for m in z:
   for g in range(1-len(d),len(k)):
    for p in range(1-len(d[0]),len(k[0])):
     if all(s:=[[e,k[g+z][p+u]][k[g+z][p+u]==m]*((k[g+z][p+u]==m)==(d[z][u]==c))for z in range(len(d))for u in range(len(d[0]))if len(k)>g+z>-1<p+u<len(k[0])])>0<s.count(m)==n.count(m):return r