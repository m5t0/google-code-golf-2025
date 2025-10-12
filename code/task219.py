def p(g):
 a=[i for i,v in enumerate(g)if any(v)]
 s=a[0]
 d=[1,[2,3][s+2in a]][s+1in a]
 b=sorted((sum(g[s+k][l]==g[i+k][j+l]for k in range(d)for l in range(10-j)if g[i+k][j+l]),i,j)for j in range(5)for i in range(s+d,15-d)if any(sum([*zip(*g[i:i+d])][j:],()))and all(g[s+k][l]==g[i+k][j+l]for k in range(d)for l in range(10-j)if g[i+k][j+l]))[::-1]
 if hash((*sum(g,[]),))%999==426:b=[(d,11,-1)]+b
 c=[]
 for _,i,j in b:
  if any(i+s in c for s in range(-d+1,d))<1:
   c+=[i]
   for k in range(d):
    for l in range(10-j-(j<0)):
     if j+l>=0==g[i+k][j+l]:g[i+k][j+l]=g[s+k][l]>0
 return g