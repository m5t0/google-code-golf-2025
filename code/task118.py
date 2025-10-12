def p(f,s=range):
 e,p=len(f),len(f[0]);d={(t,n)for t in s(e)for n in s(p)if f[t][n]&2};m=lambda i,t:[i and(m(i[1:],t)or not i[0]&t and m(i[1:],t|i[0])),t][d<=t]
 for n in 2,3:
  if t:=m([t for m in s(e)for i in s(p)for t in[{(t,n)for t in s(-n,n+1)for t,n in[(m+t,i),(m,i+t)]if e>t>-1<n<p}]if min(f[t][n]for t,n in t)&2],set()):
   for t,n in t:f[t][n]+=3*(f[t][n]&1)
   return f