def p(e):
 l={(n,a)for n in range(len(e))for a in range(len(e[0]))if e[n][a]&2}
 for a in 2,3:
  n=[n for t in range(len(e))for i in range(len(e[0]))for n in[{(n,a)for n in range(-a,a+1)for n,a in[(t+n,i),(t,i+n)]if len(e)>n>-1<a<len(e[0])}]if min(e[n][a]for n,a in n)&2];a=lambda i,n:[i and(a(i[1:],n)or not i[0]&n and a(i[1:],n|i[0])),n][l<=n]
  if n:=a(n,set()):
   for n,a in n:e[n][a]+=3*(e[n][a]&1)
   return e