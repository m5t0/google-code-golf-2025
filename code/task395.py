r=0,1,2
p=lambda g:[[2*(g[i][j]|g[i+3][j]<1)for j in r]for i in r]