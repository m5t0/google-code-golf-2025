def p(g):
 a=sum(g,[]);i,j=divmod(a.index(a:=min(a,key=a.count)),10);g=[[0]*10for _ in g]
 for y in-1,0,1:g[i+y][j-1:j+2]=2,2,2
 g[i][j]=a;return g