def p(g,r=range(10)):
 def D(i,j,P):
  if({i,j}<{*r})^1or P!=g[i][j]^1:return 0
  g[i][j]=P;return-~sum(D(i-1+I//3,j-1+I%3,P)for I in r[:9])
 a={D(i,j,9)for j in r for i in r}-{0};return[[((s:=g[i][j])>2)+(D(i,j,s^1)==min(a))for j in r]for i in r]