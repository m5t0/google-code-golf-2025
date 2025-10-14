def p(f,p=range):
 e,g=len(f),len(f[0]);n,t,d,o=max(((t-n)*(o-d),n,t,d,o)for n in p(e)for t in p(n+2,e+1)for d in p(g)for o in p(d+2,g+1)if max(max(p[d:o])for p in f[n:t])<1)[1:]
 for p in p(n,t):f[p][d:o]=[6]*(o-d)
 return f