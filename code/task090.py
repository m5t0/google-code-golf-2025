def p(g,r=range):
 m,n=len(g),len(g[0]);i,j,k,l=max(((j-i)*(l-k),i,j,k,l)for i in r(m)for j in r(i+2,m+1)for k in r(n)for l in r(k+2,n+1)if max(max(r[k:l])for r in g[i:j])<1)[1:]
 for p in r(i,j):g[p][k:l]=[6]*(l-k)
 return g