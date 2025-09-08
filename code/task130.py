s=0,1,2
p=lambda g:[[(g[3*i][3*j]-5or g[3*i][3*j+1]-5or g[3*i+1][3*j]-5)+5for j in s]for i in s]