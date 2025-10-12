def p(g):
 m,n,*t=len(g),len(g[0]);r={(a//n,a%n):sum(g,[])[a]for a in range(m*n)if sum(g,[])[a]}
 def l(i,u):
  if m>i>-1<u<n>0<((i,u)in r):
   e[i-j,u-h]=r.pop((i,u))
   for a in-1,1:l(i+a,u);l(i,u+a)
 while r:
  t+=[e:={}];j,h=min(r);l(j,h)
  if len(e)<4:t.pop()
  else:
   for i,u in e:g[j+i][h+u]=0
 k=eval(str(g))
 for e in t:
  for q in range(8):
   for a in range(m*n):
    if all(m>a//n+j[0]>-1<a%n+j[1]<n for j in e)>0<2<sum(g[a//n+j[0]][a%n+j[1]]==w for j,w in e.items()):
     for j,w in e.items():k[a//n+j[0]][a%n+j[1]]=w
   e={([-l,l][q&3>2],e):w for(e,l),w in e.items()}
 return k