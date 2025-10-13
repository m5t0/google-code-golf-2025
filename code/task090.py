def p(f,r=range):
 t,i=len(f),len(f[0]);e,o,a,n=max(((o-e)*(n-a),e,o,a,n)for e in r(t)for o in r(e+2,t+1)for a in r(i)for n in r(a+2,i+1)if max(max(r[a:n])for r in f[e:o])<1)[1:]
 for r in r(e,o):f[r][a:n]=[6]*(n-a)
 return f