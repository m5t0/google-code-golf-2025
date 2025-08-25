def p(g,r=range):
 d=[0,1,0,-1];h=[[*v]for v in g]
 for i in r(R:=len(g)):
  for j in r(R):
   if g[i][j]<1:continue
   for k in r(4):
    x=(a:=d[k])+(b:=d[(k+1)%4]);y=b+(c:=d[(k+2)%4]);e=v=1
    if R>i+a>-1<i+b<R>j+b>-1<j+c<R and g[i+a][j+b]<1>g[i+b][j+c]:
     while i+e*x<R>j+e*y and i+e*x>-1<j+e*y:
      if v>1:h[i+e*x][j+e*y]=h[i][j]
      if g[i+e*x][j+e*y]>0:v+=1
      e+=1
 return h