def p(g):
 f=[g[-i] for i in range(2,len(g))]
 g=g+f+g+f+[g[0]]
 return g
