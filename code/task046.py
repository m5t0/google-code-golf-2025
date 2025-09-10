def p(g):
 x=z=0;l=[];a=[*zip(*g)];a+=[[0]*3]*any(a[-1])
 for i,v in enumerate(a):
  if any(v)^1:
   l+=[[max(t*(t!=5)for s in a[x:i]for t in s)*(q>0)for q in p]for p in[*zip(*g[z:]+g[:z])][x:i]]
   if a[i+1:]:z+=a[i+1].index(5)-a[i-1].index(5);x=i+1
 return[*zip(*l)]