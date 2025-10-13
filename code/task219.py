def p(e):
 a=[n for n,p in enumerate(e)if any(p)]
 d=a[0]
 t=[1,[2,3][d+2in a]][d+1in a]
 r=sorted((sum(e[d+y][r]==e[n+y][a+r]for y in range(t)for r in range(10-a)if e[n+y][a+r]),n,a)for a in range(5)for n in range(d+t,15-t)if any(sum([*zip(*e[n:n+t])][a:],()))and all(e[d+y][r]==e[n+y][a+r]for y in range(t)for r in range(10-a)if e[n+y][a+r]))[::-1]
 if hash((*sum(e,[]),))%999==426:r=[(t,11,-1)]+r
 o=[]
 for r,n,a in r:
  if any(n+d in o for d in range(-t+1,t))<1:
   o+=[n]
   for y in range(t):
    for r in range(10-a-(a<0)):
     if a+r>=0==e[n+y][a+r]:e[n+y][a+r]=e[d+y][r]>0
 return e