def p(g):
 r=[[0]*len(g[0])for _ in g]
 v=set()
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]and(i,j)not in v:
    c,q=[(i,j)],[(i,j)]
    v.add((i,j))
    x=g[i][j]
    while q:
     a,b=q.pop()
     for d,e in[(0,1),(1,0),(0,-1),(-1,0)]:
      if 0<=a+d<len(g)and 0<=b+e<len(g[0])and g[a+d][b+e]==x and(a+d,b+e)not in v:
       v.add((a+d,b+e))
       c.append((a+d,b+e))
       q.append((a+d,b+e))
    h=max(a for a,b in c)-min(a for a,b in c)+1
    for a,b in c:r[a-h][b]=x
 return r