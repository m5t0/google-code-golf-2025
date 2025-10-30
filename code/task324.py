def p(g):
 n=sum(g,[]);s=sorted({*n},key=n.count);_,a,q,d=s;p,u=len(g),len(g[0])
 if sum(q in r for r in g)>sum(d in r for r in g):q,d=d,q
 s=[q in r for r in g];c=[q in r for r in zip(*g)]
 r=[(e,n)for e in range(p)for n in range(u)if g[e][n]in{_,a}]
 if a^next(g[e][n]for e,n in r if s[e]&c[n]):_,a=a,_
 return[[(d,q,_,a)[2*any(abs(e-q)==abs(n-_)for q,_ in r)+(s[e]&c[n])]for n in range(u)]for e in range(p)]