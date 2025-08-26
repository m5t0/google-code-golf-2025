def p(g,r=range):
 d=0,1,0,-1;h=[*map(list,g)]
 for i in r(R:=len(g)):
  for j in r(R):
   if g[i][j]<1:continue
   for k in r(4):
    x=(a:=d[k])+(b:=d[(k+1)%4]);y=b+(c:=d[(k+2)%4]);e=v=1
    if R>i+a>-1<i+b<R>j+b>-1<j+c<R and g[i+a][j+b]<1>g[i+b][j+c]:
     while(s:=j+e*y)>-1<(t:=i+e*x)<R>s:
      if v>1:h[t][s]=h[i][j]
      if g[t][s]:v+=1
      e+=1
 return h