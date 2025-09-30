def p(g):
 h=[[0]*9for _ in range(9)]
 for k in range(64):h[(max(g[0])<1)+k//8][(max(next(zip(*g)))<1)+k%8]=[g[0][2]or g[2][0],g[0][0]or g[2][2]][(k//8-3.5)*(k%8-3.5)>0]
 return h