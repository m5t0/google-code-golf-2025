def p(g,r=range):
 c,h,w,d,m,n,l=[],[],[],0,len(g[0]),len(g),[g]*5
 for i in r(9):c+=[i+1]*(0<sum(g,[]).count(i+1)<3)
 a=g[0][g[0][0]in c];z=sum({*sum(g,[])}-{*c,a})
 for i in r(n):
   s=g[i].count(z)
   if s>m-3:
    h+=[i]
    if s<m:d=sum({*g[i]}-{a,z})
 f=[*map(list,zip(*g))]
 for i in r(m):
   s=f[i].count(z)
   if s>n-3:
    w+=[i]
    if s<n:d=sum({*f[i]}-{a,z})
 for i in r(4):
  l=[[*map(list,zip(*j))][::-1]for j in l];v=l[i]
  for x in r(len(v)-1):
   for y in r(len(v[0])-1):
    if v[x][y]in c:v[x+1][y+1]=d;l[4][x+1][y+1]=d
 return [[l[4][j][k]if(l[4][j][k]in c)^1|(j in h)|(k in w)else sum({*c}-{d})for k in r(m)]for j in r(n)]