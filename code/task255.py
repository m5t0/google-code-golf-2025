def p(g,r=range):
 g=[[0]*32,*[[0,*v,0]for v in g],[0]*32];a=eval(str(g))
 for _ in r(8):
  i=-1;g=[*map(list,zip(*g))][::-1];a=[*map(list,zip(*a))][::-1]
  while i<33:
   i+=1;I=i
   for j in r(33,i,-1):
    for k in r(20):
     for V in a[i+1:j-1]*(sum(sum(v[:~k])for v in g[i:j])<1):
      V[:-k-2]=[3]*(30-k);i=j
      for K in 3,4:V[-k-K]-=3*(a[I][-k-K]<a[I][27-k])
 return[v[1:-1]for v in a[1:-1]]