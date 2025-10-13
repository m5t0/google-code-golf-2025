def p(e,p=range):
 f=len(e)
 for a in p(4):
  for i in p(f):
   for l in p(f-1):
    if e[i][l]==2>e[i][l+1]+1:
     u=f-l;e[i][l:]=u*[2];n=0
     while 2<e[i][l+~n]:n+=1
     for n in p(n):e[i+~n][l:]=e[i-~n][l:]=u*[3]
  e=[*map(list,zip(*e))][::-1]
 return e