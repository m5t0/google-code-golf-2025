def p(q):
 f=sum(q,[]);e=sorted({*f},key=f.count)
 for s in e:
  v=[[[e[-1],k][k==s]for*f,k in zip(*q,f)if s in f]for f in q if s in f]
  for k in e:
   for i in range(-22,22):
    for l in range(-22,22):
     if all(t:=[((q[i+e][l+h]==k)==(v[e//2][h//2]==s))*q[i+e][l+h]for e in range(len(v)*2)for h in range(len(v[0])*2)if len(q)>i+e>-1<l+h<len(q[0])])>0<t.count(k)==f.count(k):return v