e=enumerate
f=lambda g,k:[k in v for v in g].index(1)
p=lambda g:[[(w>2)*3|(g[i+f(g,2)+~f(g,3)][j+f(zip(*g),2)+~f(zip(*g),3)]==2)*2for j,w in e(v)]for i,v in e(g)]