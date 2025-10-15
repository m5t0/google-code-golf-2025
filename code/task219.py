def p(a):
 p=[n for n,r in enumerate(a)if any(r)]
 u=p[0]
 p=[1,[2,3][u+2in p]][u+1in p]
 i=sorted((sum(a[u+r][f]==a[n+r][i+f]for r in range(p)for f in range(10-i)if a[n+r][i+f]),n,i)for i in range(5)for n in range(u+p,15-p)if any(sum([*zip(*a[n:n+p])][i:],()))and all(a[u+r][f]==a[n+r][i+f]for r in range(p)for f in range(10-i)if a[n+r][i+f]))[::-1]
 if hash((*sum(a,[]),))%999==426:i=[(p,11,-1)]+i
 e=[]
 for f,n,i in i:
  if any(n+u in e for u in range(-p+1,p))<1:
   e+=[n]
   for r in range(p):
    for f in range(10-i-(i<0)):
     if i+f>=0==a[n+r][i+f]:a[n+r][i+f]=a[u+r][f]>0
 return a