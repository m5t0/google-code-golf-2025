def p(l,d=range):
 f=len(l)
 for r in d(4):
  for r in d(f):
   for p in d(f-1):
    if l[r][p]==2>l[r][p+1]+1:
     a=f-p;l[r][p:]=a*[2];s=0
     while 2<l[r][p+~s]:s+=1
     for s in d(s):l[r+~s][p:]=l[r-~s][p:]=a*[3]
  l=[*map(list,zip(*l))][::-1]
 return l