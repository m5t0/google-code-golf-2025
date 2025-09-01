d=0,1,0,-1,0
def p(g):
 for x in range(100):
  for k in[0,1,2,3]*(g[i:=x//10][j:=x%10]&1):
   if-1<(I:=i+d[k])<10>(J:=j+d[k+1])>=0:g[I][J]=[6,8,7,2][k]
 return g