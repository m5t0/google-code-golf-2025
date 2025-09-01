def p(g,r=range):
 d=0,1,0,-1,0;e={}
 def D(i,j,c):
  if(0<=i<10>j>=0)^1|((i,j)in e):return 0
  e[i,j]=c
  if g[i][j]:
   for I in r(4):g[i][j]+=D(i+d[I],j+d[I+1],c)
  return g[i][j]
 return[[[D(i,j,(i,j)),1+(g[e[i,j][0]][e[i,j][1]]==30)][g[i][j]>0]for j in r(10)]for i in r(10)]