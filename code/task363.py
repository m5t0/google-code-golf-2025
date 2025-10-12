def p(g,r=range(10)):
 I=sum(g,[]).index(2);a=[(i-I//10,j-I%10)for i in r for j in r if g[i][j]&2]
 for I,J in(g[0][5:7]==[0,2])*a:g[1+I][8+J]=2
 for j in r:
  for i in r:
   for I,J in a*all(i+x<10>j+y>=g[i+x][j+y]<1for x,y in a):g[i+I][j+J]=2
 if g[5].count(2)>7:g[1][3:7]=[0]*4
 return g