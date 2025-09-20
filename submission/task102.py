def p(g,r=range):
 h=[*zip(*g)]
 for k in r(144):x,y=k//12,k%12;[exec("v[y+1:w]=[2]*(w+~y)")for l in r(2,12-max(x,y))if min(g[x][y:(w:=y+l)]+g[z:=x+l][y:w]+[*h[y][x:z]+h[w][x:z]])+1>5>max(sum((g[i][y+1:w]for i in r(x+1,z)),[]))for v in g[x+1:z]]
 return g