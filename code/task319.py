def p(q):
 f=sum(q,[]);_=max(f,key=f.count);e=sorted({*f}-{_})
 for s in e:
  o=[[[_,k][k==s]for*f,k in zip(*q,f)if s in f]for f in q if s in f];v=[[k for k in o for s in'00']for o in o for s in'00']
  for k in e:
   for i in range(1-len(v),len(q)):
    for l in range(1-len(v[0]),len(q[0])):
     if all(t:=[[_,q[i+e][l+h]][q[i+e][l+h]==k]*((q[i+e][l+h]==k)==(v[e][h]==s))for e in range(len(v))for h in range(len(v[0]))if len(q)>i+e>-1<l+h<len(q[0])])>0<t.count(k)==f.count(k):return o