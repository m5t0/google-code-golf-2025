def p(f):
 u=sum(f,[]);e=max(u,key=u.count);k=sorted({*u}-{e})
 for g in k:
  j=[[[e,l][l==g]for*u,l in zip(*f,u)if g in u]for u in f if g in u];q=[[l for l in r for i in'00']for r in j for i in'00']
  for t in k:
   for w in range(1-len(q),len(f)):
    for a in range(1-len(q[0]),len(f[0])):
     if all(s:=[[e,f[w+x][a+y]][f[w+x][a+y]==t]*((f[w+x][a+y]==t)==(q[x][y]==g))for x in range(len(q))for y in range(len(q[0]))if len(f)>w+x>-1<a+y<len(f[0])])>0<s.count(t)==u.count(t):return j