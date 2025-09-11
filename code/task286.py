def p(g):
 def D(i,j,P,o=1):
  for k in[-1,1]*((m>j>-1<i<n)*P%8>=1>g[i][j]*o):g[i][j]=P;D(i+k,j,x:=sum({*sum(g,[])})-8-P);D(i,j+k,x)
 n=len(g);m=len(g[0]);[D(i%n,I:=i//n,g[i%n][I],0)for i in range(n*m)];return g