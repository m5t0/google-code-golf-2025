e=enumerate
f=lambda g:[i for i,v in e(g)if 2in v][0]
p=lambda g:[[(w>2)*3or(g[i+f(g)-(x:=sum(g,[]).index(3))//(l:=len(v))-1][j+f(zip(*g))-x%l-1]==2)*2for j,w in e(v)]for i,v in e(g)]