def p(p):
 n=sum(p,[]);c=sorted({*n},key=n.count);_,a,q,d=c;e,s=len(p),len(p[0])
 if sum(q in r for r in p)>sum(d in r for r in p):q,d=d,q
 c=[q in r for r in p];u=[q in r for r in zip(*p)]
 r=[(e,n)for e in range(e)for n in range(s)if p[e][n]in{_,a}]
 if a^next(p[e][n]for e,n in r if c[e]&u[n]):_,a=a,_
 return[[(d,q,_,a)[2*any(abs(e-q)==abs(n-_)for q,_ in r)+(c[e]&u[n])]for n in range(s)]for e in range(e)]