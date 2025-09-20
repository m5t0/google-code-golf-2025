def p(g):
 for i in range(len(g)):
  for j in range(len(g[0])):
   if len({*str([*zip(*g[i-1:i+2])][j-1:j+2])})==7:g[i][j]=0
 return g