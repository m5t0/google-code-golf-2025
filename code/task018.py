def p(g):
 m,n=len(g),len(g[0]);t=[];r={(k//n,k%n):w for k in range(m*n)if(w:=g[k//n][k%n])}
 def f(i,j):
  if m>i>-1<j<n and(i,j)in r:s[i-u[0],j-u[1]]=r.pop((i,j));f(i+1,j);f(i-1,j);f(i,j+1);f(i,j-1)
 while r:
  t+=[s:={}];u=min(r);f(*u)
  if len(s.keys())<4:t=t[:-1]
  else:
   for x,y in s:g[u[0]+x][u[1]+y]=0
 h=eval(str(g))
 for s in t:
  for _ in range(8):
   for k in range(m*n):
    if all(m>k//n+v[0]>-1<k%n+v[1]<n for v in s.keys())>0<2<sum(g[k//n+v[0]][k%n+v[1]]==w for v,w in s.items()):
     for v,w in s.items():h[k//n+v[0]][k%n+v[1]]=w
   s={([-f,f][_%4==3],e):w for(e,f),w in s.items()}
 return h