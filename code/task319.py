def p(q):
 n=sum(q,[]);e=max(n,key=n.count);l=sorted({*n}-{e})
 for c in l:
  a=[[[e,f][f==c]for*n,f in zip(*q,n)if c in n]for n in q if c in n];d=[[f for f in r for _ in'00']for r in a for _ in'00']
  for m in l:
   for y in range(1-len(d),len(q)):
    for h in range(1-len(d[0]),len(q[0])):
     if all(s:=[[e,q[y+z][h+u]][q[y+z][h+u]==m]*((q[y+z][h+u]==m)==(d[z][u]==c))for z in range(len(d))for u in range(len(d[0]))if len(q)>y+z>-1<h+u<len(q[0])])>0<s.count(m)==n.count(m):return a