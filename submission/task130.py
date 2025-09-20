s=0,3,6
p=lambda g:[[(g[i][j]-5or g[i][j+1]-5or g[i+1][j]-5)+5for j in s]for i in s]