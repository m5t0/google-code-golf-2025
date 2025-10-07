e=enumerate
f=lambda g,k:[i for i,v in e(g)if k in v][0]
p=lambda g:[[(w>2)*3or(g[i+f(g,2)+~f(g,3)][j+f(zip(*g),2)+~f(zip(*g),3)]==2)*2for j,w in e(v)]for i,v in e(g)]