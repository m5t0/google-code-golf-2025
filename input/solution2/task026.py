def p(g):
    r=range
    return[[8if g[i][j]==g[i][j+4]==0else 0for j in r(3)]for i in r(5)]