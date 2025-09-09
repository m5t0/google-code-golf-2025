def p(g):
 def D(i,j,P,o):
  if(m>j>-1<i<n)*P%8and g[i][j]*o<1:g[i][j]=P;[D(i+I//3,~-j+I%3,sum({*sum(g,[])})-8-P,1)for I in[-2,0,2,4]]
 n=len(g);m=len(g[0]);[D(i%n,I:=i//n,g[i%n][I],0)for i in range(n*m)];return g