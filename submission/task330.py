def p(g):
 f=lambda i,j:0<=i<10>j>-1 and g[i][j]==v and(g[i].__setitem__(j,k)or 1+f(i+1,j)+f(i-1,j)+f(i,j+1)+f(i,j-1))
 for t in range(99):i=t//10;j=t%10;v=5;k=3;k=1+(f(i,j)==6);v=3;f(i,j)
 return g