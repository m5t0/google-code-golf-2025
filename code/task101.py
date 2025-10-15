def p(g):
 f,*r={(t,a):e for t,e in enumerate(g)for a,e in enumerate(e)if e},
 def m(t,a):
  if(t,a)in f:[j,e][f.pop((t,a))-1]+=[(t-_,a-k)];m(t,a+1),m(t,a-1),m(t+1,a),m(t-1,a)
 while f:
  j,e=[],[];_,k=next(i for i in f if f[i]==2);m(_,k)
  if j:r,u=j,e;f=dict(sorted(f.items()))
  elif r:
   e=max(e for e in(1,2,3)if g[_+e-1:]and g[0][k+e-1:]and{g[_+i//e][k+i%e]for i in range(e*e)}=={2})
   for t,a in r+u:
    for i in range(e*e):
     if k+a*e+i%e>=0:g[l:=_+t*e+i//e][k+a*e+i%e]=1+((t,a)in u);f.pop((l,k+a*e+i%e),1)
  else:f|={(_+t,k+a):g[_+t][k+a]for t,a in j+e}
 return g