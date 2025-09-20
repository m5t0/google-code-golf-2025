def p(g):
 for j,w in enumerate(zip(*g)):g[-1][j]=4*(sum([v>0for v in w])==1)
 return g