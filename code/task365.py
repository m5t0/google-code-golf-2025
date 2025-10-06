f=lambda v:v[:[*v,0].index(0)]
p=lambda g,e=enumerate:max((str(s:=[f(g[i+I][j:])for I,_ in e(f(w[i:]))]).count('2'),-i-j,s)for j,w in e(zip(*g))for i,_ in e(g))[2]