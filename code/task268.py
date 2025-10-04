def p(g,r=range):
 n=len(g);q=1
 for _ in r(4):
  a,h=zip(*((i,j)for i in r(n)for j in r(n)if g[i][j]));a,x,c,d=min(a),max(a),min(h),max(h);t=g[a][c];l=g[a].count(t)
  if(l<g[x].count(t))&q:
   q,h,m=0,c+l//2,d-l//2
   for t in r(x):g[t][h:m+1]=[4]*(m-h+1)
   for t in r(a+1,x):g[t][c+1:d]=[4]*(d-c-1)
   for u in r(a+1):
    if h>=u:g[a-u][h-u]=4
    if m+u<n:g[a-u][m+u]=4
  g=[*map(list,zip(*g[::-1]))]
 return g