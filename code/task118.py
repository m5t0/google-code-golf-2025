def p(e,b=range):
 r,f=len(e),len(e[0]);a={(n,t)for n in b(r)for t in b(f)if e[n][t]&2};l=lambda i,n:[i and(l(i[1:],n)or not i[0]&n and l(i[1:],n|i[0])),n][a<=n]
 for t in 2,3:
  if n:=l([n for l in b(r)for i in b(f)for n in[{(n,t)for n in b(-t,t+1)for n,t in[(l+n,i),(l,i+n)]if r>n>-1<t<f}]if min(e[n][t]for n,t in n)&2],set()):
   for n,t in n:e[n][t]+=3*(e[n][t]&1)
   return e