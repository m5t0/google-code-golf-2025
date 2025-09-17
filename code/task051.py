def p(g,r=range):
 v=sum(g,[]);x,y=divmod(v.index(min(v,key=v.count)),n:=len(g[0]))
 for k in r(9):
  if(s:=k//3-1,t:=k%3-1)!=(0,0)and s*t==0and g[x-s][y-t]<1:return[[g[i][j]or((i-x)*t==(j-y)*s and(s and(i-x)//s>0 or t and(j-y)//t>0))*g[x][y]for j in r(n)]for i in r(len(g))]