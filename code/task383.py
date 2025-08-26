def p(g,r=range):
 H,W=len(g),len(g[0]);a=[i for i in r(H) if sum(g[i][j]>0 for j in r(W))>0];b=[j for j in r(W) if sum(g[i][j]>0 for i in r(H))>0];y,z=g[a[0]][b[0]],g[a[2]][b[2]]
 return [[[g[i][j],[z,y][g[i][j]>0]][0<sum(x==y for x in g[i])<4or 0<sum(x==y for x in [row[j]for row in g])<4]for j in r(W)]for i in r(H)]

