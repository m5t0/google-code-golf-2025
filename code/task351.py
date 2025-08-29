p=lambda g,r=range(16):[[g[15-i][15-j]for j in r if g[i][j]==3]for i in r if any(g[i][j]==3for j in r)]
