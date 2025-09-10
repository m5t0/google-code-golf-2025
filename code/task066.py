def p(g,e=enumerate):
 h=[(i,j)for i,v in e(g)for j,w in e(v)if w==3]
 def f(i,j,x,y,c):
  i+=x;j+=y;v=0
  if c>2or not(g[i:i+1]and g[i][j:j+1])or(v:=(t:=g[i])[j]):return(v==2)*2+(v>5)
  t[j]=3;b=f(i,j,x,y,c);c+=1
  if b>1or b and(f(i,j,-y,-x,c)>1or f(i,j,y,x,c)>1):return 2
  t[j]=0;return 0
 for(i,j),(k,l)in h,h[::-1]:
  if f(i,j,i-k,j-l,0)>1:return g