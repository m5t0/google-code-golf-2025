f=lambda g:sorted({j for j in range(20)for v in g if(v[j-1]-v[j])*v[j]})
p=lambda g:[[g[i][j]for j in f(g)]for i in f([*zip(*g)])]