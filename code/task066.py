def p(g,e=enumerate):
 m,n=len(g),len(g[0]);h=[(i,j)for i,v in e(g)for j,w in e(v)if w==3][:2]
 def f(i,j,x,y,c):
  if(m>i>-1<j<n)^1or c>3:return 0
  if(v:=g[i][j]):return(v==2)+(v!=3)
  g[i][j]=3;b=f(i+x,j+y,x,y,c)
  if b>1:return 2
  if b and(f(i-y,j-x,-y,-x,c+1)>1or f(i+y,j+x,y,x,c+1)>1):return 2
  g[i][j]=0;return 0
 for k in 0,1:
  a,b=h[k],h[k-1];x=a[0]-b[0];y=a[1]-b[1]
  if f(a[0]+x,a[1]+y,x,y,0)>1:return g