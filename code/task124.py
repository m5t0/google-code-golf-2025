def p(g,r=range):
 m,n=len(g),len(g[0])
 for k in r(1,10):
  x=k//3;y=k%3
  if all(1-(v[j]>0)^(w[j+y]>0)for v,w in zip(g,g[x:])for j in r(n-y)):
   h=[v+[0]*(10-n)for v in g]+[[0]*10for _ in r(10-m)]
   for l in r(100):h[i][j]=h[i:=l//10][j:=l%10]or(i-x>-1<j-y)*h[i-x][j-y]
   return h