def p(g,r=range):
 d=0,1,0,-1;c=[*map(list,g)]
 for i in r(b:=len(g)):
  for j in r(b):
   if g[i][j]!=0:
    for k in r(4):
     e=v=1
     if b>i+d[k]>-1<i+d[(k+1)%4]<b>j+d[(k+1)%4]>-1<j+d[(k+2)%4]<b and g[i+d[k]][j+d[(k+1)%4]]<1>g[i+d[(k+1)%4]][j+d[(k+2)%4]]:
      while(s:=j+e*(d[(k+1)%4]+d[(k+2)%4]))>-1<(t:=i+e*(d[k]+d[(k+1)%4]))<b>s:
       if v>=2:c[t][s]=c[i][j]
       if g[t][s]:v+=1
       e+=1
 return c