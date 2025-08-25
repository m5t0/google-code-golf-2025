def p(g,r=range):
 for i in r(12):
  if sum(x==2for x in g[i])>4:
   for j in r(2,4):
    for k in r(12):g[i-j if i<7else i+j][k],g[i+j if i<7else i-j][k]=g[i+j if i<7else i-j][k],0
 for j in r(12):
  if sum(g[i][j]==2for i in r(12))>4:
   for i in r(2,4):
    for k in r(12):g[k][j-i if j<7else j+i],g[k][j+i if j<7else j-i]=g[k][j+i if j<7else j-i],0
 return g