def p(a,p=range):
 f,e=len(a),len(a[0]);t,m,o,r,x=max(((o-m)*(x-r),m,o,r,x)for m in p(f)for o in p(m+2,f+1)for r in p(e)for x in p(r+2,e+1)if 1>max(max(m[r:x])for m in a[m:o]))
 for o in p(m,o):a[o][r:x]=[6]*(x-r)
 return a