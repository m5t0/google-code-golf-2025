p=lambda g,h=2,w=6:[[g[h-1-i][j]if j%2 else g[i][j]for j in range(w)]for i in range(h)]
