def p(g):
 m,n,*t=len(g),len(g[0]);r={(k//n,k%n):sum(g,[])[k]for k in range(m*n)if sum(g,[])[k]}
 def f(i,j):
  if m>i>-1<j<n>0<((i,j)in r):
   s[i-u[0],j-u[1]]=r.pop((i,j))
   for k in-1,1:f(i+k,j);f(i,j+k)
 while r:
  t+=[s:={}];u=min(r);f(*u)
  if len(s)<4:t.pop()
  else:
   for x,y in s:g[u[0]+x][u[1]+y]=0
 h=eval(str(g))
 for s in t:
  for _ in range(8):
   for k in range(m*n):
    if all(m>k//n+v[0]>-1<k%n+v[1]<n for v in s)>0<2<sum(g[k//n+v[0]][k%n+v[1]]==w for v,w in s.items()):
     for v,w in s.items():h[k//n+v[0]][k%n+v[1]]=w
   s={([-f,f][_&3>2],e):w for(e,f),w in s.items()}
 return h