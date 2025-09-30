r=range
p=lambda g:[[max(g[k//7][k%7]for k in r((i+j)%3,49,3))for j in r(7)]for i in r(7)]