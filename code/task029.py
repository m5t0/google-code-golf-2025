def p(g,e=enumerate):
 for x in range(10):
  if s:=[*zip(*[(i,j)for i,v in e(g)for j,w in e(v)if w==x])]:
   a,b,c,d=min(s[0]),max(s[0]),min(s[1]),max(s[1])
   if len({*((g[a]+g[b])[c:d+1]+(h:=[*map(list,zip(*g[a:b+1]))])[c]+h[d])})<2:return[*map(list,zip(*h[c+1:d]))][1:-1]