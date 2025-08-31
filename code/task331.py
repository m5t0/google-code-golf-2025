def p(g,r=range):
 d=0,1,0,-1,0
 for x in r(100):
  for k in [*r(4)]*(g[i:=x//10][j:=x%10]==1):
   if 0<=(I:=i+d[k])<10>(J:=j+d[k+1])>=0:g[I][J]=[6,8,7,2][k]
 return g