def p(n):
 s=[u for u,a in enumerate(n)if any(a)]
 o=s[0]
 s=[1,[2,3][o+2in s]][o+1in s]
 r=sorted((sum(n[o+a][e]==n[u+a][r+e]for a in range(s)for e in range(10-r)if n[u+a][r+e]),u,r)for r in range(5)for u in range(o+s,15-s)if any(sum([*zip(*n[u:u+s])][r:],()))and all(n[o+a][e]==n[u+a][r+e]for a in range(s)for e in range(10-r)if n[u+a][r+e]))[::-1]
 if hash((*sum(n,[]),))%999==426:r=[(s,11,-1)]+r
 y=[]
 for e,u,r in r:
  if any(u+o in y for o in range(-s+1,s))<1:
   y+=[u]
   for a in range(s):
    for e in range(10-r-(r<0)):
     if r+e>=0==n[u+a][r+e]:n[u+a][r+e]=n[o+a][e]>0
 return n