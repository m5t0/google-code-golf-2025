def p(f):
 z=range;e=sum(f,[]);j=sorted({*e},key=e.count);o,s,a,b=j;m,n=len(f),len(f[0])
 if sum(a in r for r in f)>sum(b in r for r in f):a,b=b,a
 j=[a in r for r in f];q=[a in r for r in zip(*f)]
 r=[(u,e)for u in z(m)for e in z(n)if f[u][e]in{o,s}]
 if s^next(f[u][e]for u,e in r if j[u]&q[e]):o,s=s,o
 return[[(b,a,o,s)[2*any(abs(u-k)==abs(e-o)for k,o in r)+(j[u]&q[e])]for e in z(n)]for u in z(m)]