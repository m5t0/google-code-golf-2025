def p(c):
 z=range;a=sum(c,[]);d=sorted({*a},key=a.count);f,_,p,e=d;q,s=len(c),len(c[0])
 if sum(p in r for r in c)>sum(e in r for r in c):p,e=e,p
 d=[p in r for r in c];b=[p in r for r in zip(*c)]
 r=[(n,a)for n in z(q)for a in z(s)if c[n][a]in{f,_}]
 if _^next(c[n][a]for n,a in r if d[n]&b[a]):f,_=_,f
 return[[(e,p,f,_)[2*any(abs(n-t)==abs(a-f)for t,f in r)+(d[n]&b[a])]for a in z(s)]for n in z(q)]