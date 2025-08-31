def p(g,r=range):
 m=len(g);n=len(g[0]);x,y=[(i//n,i%n)for i in r(m*n)if sum(w==g[i//n][i%n]for v in g for w in v)][0]
 for s,t in(0,1),(0,-1),(1,0),(-1,0):
  if g[x-s][y-t]<1:return[[g[i][j]or((i-x)*t==(j-y)*s and((i-x)*s>0 or(j-y)*t>0))*g[x][y]for j in r(n)]for i in r(m)]