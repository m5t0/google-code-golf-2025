def p(g,r=range):
 for i in r(81):
  for j in r(9):
   if(a:=j//3-1)|(b:=j%3-1)and(c:=7-3*(a*b!=0))==10-3*g[i//9][i%9]and g[n:=i//9+a][m:=i%9+b]<1:g[n][m]=c
 return g