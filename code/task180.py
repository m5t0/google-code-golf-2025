r=0,1,2,3
p=lambda g:[[g[i][j+4]or(w:=g[i+4])[j]or w[j+4]or g[i][j]for j in r]for i in r]