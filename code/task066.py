def p(g,e=enumerate):
 def f(i,j,x,y,c):
  i+=x;j+=y;v=0
  if c>2or not(g[i:i+1]and(t:=g[i])[j:j+1])or(v:=t[j]):return v>5or v==2and 2
  t[j]=3;b=f(i,j,x,y,c)
  if b>1or b and(f(i,j,-y,-x,c+1)>1or f(i,j,y,x,c+1)>1):return 2
  t[j]=0;return 0
 for(i,j),(k,l)in(h:=[(i,j)for i,v in e(g)for j,w in e(v)if w==3]),h[::-1]:
  if f(i,j,i-k,j-l,0)>1:return g