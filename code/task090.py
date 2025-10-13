def p(f,m=range):
 o,g=len(f),len(f[0]);n,x,e,l=max(((x-n)*(l-e),n,x,e,l)for n in m(o)for x in m(n+2,o+1)for e in m(g)for l in m(e+2,g+1)if max(max(m[e:l])for m in f[n:x])<1)[1:]
 for m in m(n,x):f[m][e:l]=[6]*(l-e)
 return f