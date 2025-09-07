s=0,1,2
p=lambda g:[[+(sum(g[4*i+k//3][4*j+k%3]for k in range(9))>9)for j in s]for i in s]