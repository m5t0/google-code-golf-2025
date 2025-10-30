def p(t):
 for i in range(4):
  for i in range(len(t)):
   for p in range(len(t)-1):
    if t[i][p]==2>t[i][p+1]+1:
     w=len(t)-p;t[i][p:]=w*[2];l=0
     while 2<t[i][p+~l]:l+=1
     for l in range(l):t[i+~l][p:]=t[i-~l][p:]=w*[3]
  t=[*map(list,zip(*t))][::-1]
 return t