def p(g):
 r,*c={(i,j):v for i,v in enumerate(g)for j,v in enumerate(v)if v},
 def f(i,j):
  if(i,j)in r:[a,b][r.pop((i,j))-1]+=[(i-x,j-y)];f(i,j+1),f(i,j-1),f(i+1,j),f(i-1,j)
 while r:
  a,b=[],[];x,y=next(k for k in r if r[k]==2);f(x,y)
  if a:c=a;e=b;r=dict(sorted(r.items()))
  elif c:
   d=max(d for d in(1,2,3)if g[x+d-1:]and g[0][y+d-1:]and{g[x+k//d][y+k%d]for k in range(d*d)}=={2})
   for i,j in c+e:
    for k in range(d*d):
     if y+j*d+k%d>=0:g[s:=x+i*d+k//d][y+j*d+k%d]=1+((i,j)in e);r.pop((s,y+j*d+k%d),1)
  else:r|={(x+i,y+j):g[x+i][y+j]for i,j in a+b}
 return g