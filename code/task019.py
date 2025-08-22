def p(g):
 h,w,R,o=len(g),len(g[0]),range,[r+r for r in g+g]
 for i in R(2*h):
  for j in R(2*w):
   for Y in i-1,i+1:
    for X in j-1,j+1:
     if g[i%h][j%w]and-1<Y<2*h and-1<X<2*w:o[Y][X]=o[Y][X]or 8
 return o