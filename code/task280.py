def p(l,m=range):
 f=len(l)
 for r in m(4):
  for r in m(f):
   for n in m(f-1):
    if l[r][n]==2>l[r][n+1]+1:
     w=f-n;l[r][n:]=w*[2];i=0
     while 2<l[r][n+~i]:i+=1
     for i in m(i):l[r+~i][n:]=l[r-~i][n:]=w*[3]
  l=[*map(list,zip(*l))][::-1]
 return l