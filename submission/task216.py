f=lambda v:v[:[*v,0].index(0)]
p=lambda g,e=enumerate:max(([f(g[i+I][j:])for I,_ in e(f(w[i:]))]for j,w in e(zip(*g))for i,_ in e(g)),key=lambda g:str(g).count('2'))