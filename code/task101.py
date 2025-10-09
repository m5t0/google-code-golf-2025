def p(g):
 r,*c={(i,j):v for i,v in enumerate(g)for j,v in enumerate(v)if v},
 def f(i,j):
  if(i,j)in r:[a,b][r.pop((i,j))-1]+=[(i-x,j-y)];f(i,j+1);f(i,j-1);f(i+1,j);f(i-1,j)
 while r:
  a,b=[],[];x,y=[(x,y)for(x,y),v in r.items()if v==2][0];f(x,y)
  if a:c=a;e=b;r={(i,j):r[i,j]for i,j in sorted(r)}
  elif c:
   d=max(d for d in(1,2,3)if g[x+d-1:]and[*zip(*g)][y+d-1:]and{*sum([*zip(*g[x:x+d])][y:y+d],())}=={2})
   for i,j in c+e:
    for k in range(d*d):
     if(t:=y+j*d+k%d)>=0:g[s:=x+i*d+k//d][t]=1+((i,j)in e);r.pop((s,t),1)
  else:r|={(x+i,y+j):g[x+i][y+j]for i,j in a+b}
 return g