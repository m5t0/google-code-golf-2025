def p(g):
 def D(i,j,o=1):
  for k in[-1,1]*(n>i>-1<j<n>1>o*g[i][j]):g[i][j]=1;D(i+k,j);D(i,j+k)
 n=len(g);[g[i//n][i%n]-1or D(i//n,i%n,0)for i in range(n*n)];return g