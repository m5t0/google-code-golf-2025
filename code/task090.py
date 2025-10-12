def p(m,r=range):
 q,g=len(m),len(m[0]);e,f,n,i=max(((f-e)*(i-n),e,f,n,i)for e in r(q)for f in r(e+2,q+1)for n in r(g)for i in r(n+2,g+1)if max(max(r[n:i])for r in m[e:f])<1)[1:]
 for r in r(e,f):m[r][n:i]=[6]*(i-n)
 return m