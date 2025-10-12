def p(s):
 d=[i for i,a in enumerate(s)if any(a)]
 p=d[0]
 d=[1,[2,3][p+2in d]][p+1in d]
 r=sorted((sum(s[p+a][e]==s[i+a][r+e]for a in range(d)for e in range(10-r)if s[i+a][r+e]),i,r)for r in range(5)for i in range(p+d,15-d)if any(sum([*zip(*s[i:i+d])][r:],()))and all(s[p+a][e]==s[i+a][r+e]for a in range(d)for e in range(10-r)if s[i+a][r+e]))[::-1]
 if hash((*sum(s,[]),))%999==426:r=[(d,11,-1)]+r
 g=[]
 for e,i,r in r:
  if any(i+p in g for p in range(-d+1,d))<1:
   g+=[i]
   for a in range(d):
    for e in range(10-r-(r<0)):
     if r+e>=0==s[i+a][r+e]:s[i+a][r+e]=s[p+a][e]>0
 return s