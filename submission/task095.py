p=lambda g:[exec("g[k//9+l//3-1][k%9+l%3-1]=1")for k in range(81)for l in[0,1,2,3,5,6,7,8]*(g[k//9][k%9]==5)]and g



s=0,1,8
p=lambda g,r=range(9):[[g[i][j]or max(g[i-k][j-l]for k in s for l in s)>0for j in r]for i in r]