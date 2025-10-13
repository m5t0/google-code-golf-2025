def p(l,r=range):
 q,b=len(l),len(l[0]);e,f,n,u=max(((f-e)*(u-n),e,f,n,u)for e in r(q)for f in r(e+2,q+1)for n in r(b)for u in r(n+2,b+1)if max(max(r[n:u])for r in l[e:f])<1)[1:]
 for r in r(e,f):l[r][n:u]=[6]*(u-n)
 return l