def p(e,p=range):
 f=len(e)
 for a in p(4):
  for a in p(f):
   for l in p(f-1):
    if e[a][l]==2>e[a][l+1]+1:
     r=f-l;e[a][l:]=r*[2];n=0
     while 2<e[a][l+~n]:n+=1
     for n in p(n):e[a+~n][l:]=e[a-~n][l:]=r*[3]
  e=[*map(list,zip(*e))][::-1]
 return e