def p(g,r=range):
 m=len(g);n=len(g[0]);x,y=[(i//n,i%n)for i in r(m*n)if [g[i//n][i%n]]==[c for c in r(10)if sum([w==c for v in g for w in v])==1]][0]
 for k in r(9):
  if(s:=k//3-1,t:=k%3-1)!=(0,0)and s*t==0and g[x-s][y-t]<1:return[[g[i][j]or((i-x)*t==(j-y)*s and(s and(i-x)//s>0 or t and(j-y)//t>0))*g[x][y]for j in r(n)]for i in r(m)]