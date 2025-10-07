def p(g):n=len(g);return[[g[i][j]or(i+j==n-1)*2+4*(i==n-1)for j in range(n)]for i in range(n)]



p=lambda g:[[g[0][0]]+(g[0]+[2]+g[0][1:])[i:i+14]for i in range(len(g))]


p=lambda g,e=enumerate:[[w[i]or(v[j]*4//5)or(i+j==14)*2for j,w in e(g)]for i,v in e(g[::-1])]