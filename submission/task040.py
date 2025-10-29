f=lambda g:[[v[j]and v[-(j>4)]or v[j]for j in range(10)]for v in zip(*g)]
p=lambda g:f(f(g))