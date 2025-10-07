p=lambda g:(a:=[v+[*w]for v,w in zip(g,zip(*g[::-1]))])+[v[::-1]for v in a[::-1]]


p=lambda g:[[*(a:=g+[*zip(*g)][::-1])[i],*a[~i][::-1]]for i in range(6)]