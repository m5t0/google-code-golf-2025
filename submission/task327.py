def p(g):
 w=[[0]*6];g=w+[v+[0]*3for v in g]+w*3
 for i in range(6):g[i+1]=[*map(sum,zip([0]+g[i],g[i+1]))]
 return g[1:]