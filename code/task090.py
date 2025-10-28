def p(a,f=range):
 t,x=len(a),len(a[0]);o,m,e,r,n=max(((e-m)*(n-r),m,e,r,n)for m in f(t)for e in f(m+2,t+1)for r in f(x)for n in f(r+2,x+1)if 1>max(max(m[r:n])for m in a[m:e]))
 for e in f(m,e):a[e][r:n]=[6]*(n-r)
 return a