def p(g,r=range):
 d=0,1,0,-1;h=[*map(list,g)]
 for i in r(R:=len(g)):
  for j in r(R):
   if g[i][j]==0:continue
   for k in r(4):
    e=v=1
    if R>i+d[k]>-1<i+d[(k+1)%4]<R>j+d[(k+1)%4]>-1<j+d[(k+2)%4]<R and g[i+d[k]][j+d[(k+1)%4]]<1>g[i+d[(k+1)%4]][j+d[(k+2)%4]]:
     while(s:=j+e*(d[(k+1)%4]+d[(k+2)%4]))>-1<(t:=i+e*(d[k]+d[(k+1)%4]))<R>s:
      if v>=2:h[t][s]=h[i][j]
      if g[t][s]:v+=1
      e+=1
 return h