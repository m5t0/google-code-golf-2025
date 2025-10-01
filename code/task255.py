def p(g,r=range):
 n=len(g);g=[[0]*(n+2),*[[0]+v+[0]for v in g],[0]*(n+2)];a=[l.copy()for l in g];t=lambda b:list(map(list,(zip(*b))))[::-1]
 for b in r(8):
  i=0
  while i<n+3:
   h=0;
   for j in r(min(n+3,i+15),i+2,-1):
    for k in r(20):
     if sum([sum(v[:-k-1])for v in g[i:j]])==0:
      for J in r(i+1,j-1):
        a[J][:-k-2]=[3]*(n+2-k-2);
        for K in r(2):a[J][n-k-1-K]=0if(a[i][n-k-1-K]<1)&a[i][n-k-3]else 3
      i=j+2;h=1;break
    if h:break
   if h==0:i+=1
  g=t(g);a=t(a)
 return [[x for x in v[1:-1]]for v in a[1:-1]]