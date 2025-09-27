def p(g,e=enumerate):
 v=sum(g,[]);*a,c,_=sorted({*v},key=v.count);m,n=len(g),len(g[0]);b={k:[(i//n,i%n)for i,w in e(v)if w==k]for k in[c]+a};r={*sum(b.values(),[])};b.pop(c);h={}
 def f(i,j):
  if m>i>-1<j<n and(v:=g[i][j])and(i,j)in r:
   r.remove((i,j));s[v]+=i*n+j,
   for k in-1,1:f(i+k,j);f(i,j+k)
 while r:
  s={k:[]for k in[c]+a};f(*min(r))
  if s[c]:
   u,v,w=[s[i][0]for i in a[:3]];d=lambda k:(k//n-u//n,k%n-u%n);h[d(v),d(w)]=[d(k)for k in s[c]]
   for i in sum(s.values(),[]):g[i//n][i%n]=0
   for v in a:b[v].remove(((w:=min(s[v]))//n,w%n))
 for i,j in b[a[0]]:
  for k,l in h.items():
   for _ in 0,1:
    for _ in[0]*4:
     for x,y in l*all((i+x,j+y)in b[a[K+1]]for K,(x,y) in e(k)):g[i+x][j+y]=c
     k=[(-t[1],t[0])for t in k];l=[(-t,s)for s,t in l];m,n=n,m
    k=[(-t[0],t[1])for t in k];l=[(-s,t)for s,t in l]
 return g

def p(d):
 G=len(d);H=len(d[0]);R=[];K=set();V={*K}
 for r in range(G):
  for c in range(H):
   if(v:=d[r][c])and(P:=(v,r,c))not in V:
    C=[P];V.add(P)
    for J in C:
     for a,b in(0,1),(0,-1),(1,0),(-1,0):
      if G>(A:=J[1]+a)>-1<(D:=J[2]+b)<H and(w:=d[A][D])and(N:=(w,A,D))not in V:V.add(N);C.append(N)
    if len(C)>3:R+=[C]
    else:K.update(C)
 for B in R:
  Z=[*zip(*B)];Ro,Co=min(Z[1]),min(Z[2]);L=[(v,r-Ro,c-Co)for v,r,c in B]
  if C:=next((Ca for W in range(3,7)if(T:=9-W)and(Y:=[[(v,[W-1-c,c,T-1-r,c][i],[r,T-1-r,c,r][i])for v,r,c in L]for i in range(4)])if(C:=next((Ca for Cl in Y for A in range(-6,G)for D in range(-6,H)if(Ca:=[(v,r+A,c+D)for v,r,c in Cl])and all(G>p[1]>-1<p[2]<H for p in Ca)and sum(p in K for p in Ca)==3),0))),0):
   for v,r,c in C:d[r][c]=v
   for v,r,c in B:d[r][c]=0
 return d