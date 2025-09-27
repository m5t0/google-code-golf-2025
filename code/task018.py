def p(g,e=enumerate):
 v=sum(g,[]);*a,c,_=sorted({*v},key=v.count);m,n=len(g),len(g[0]);b={k:[(i//n,i%n)for i,w in e(v)if w==k]for k in[c]+a};r=sum(b.values(),[]);h={}
 def f(i,j):
  if m>i>-1<j<n and(v:=g[i][j])and(i,j)in r:r.remove((i,j));s[v]+=[(i,j)];f(i+1,j);f(i-1,j);f(i,j+1);f(i,j-1)
 while r:
  s={k:[]for k in b};f(*r[0])
  if s[c]:
   u,v,w=[s[i][0]for i in a];d=lambda k:(k[0]-u[0],k[1]-u[1]);h[d(v),d(w)]=[d(k)for k in s[c]]
   for i,j in sum(s.values(),[]):b[g[i][j]].remove((i,j));g[i][j]=0
 for i,j in b[a[0]]:
  for k,l in h.items():
   for _ in range(8):
    for x,y in l*all((i+x,j+y)in b[a[K+1]]for K,(x,y)in e(k)):g[i+x][j+y]=c
    k,l=[[([-t,t][_%4==3],s)for s,t in v]for v in(k,l)];m,n=n,m
 return g