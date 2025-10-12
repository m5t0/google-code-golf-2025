f=lambda l,i:l[i].count(1)>0<l[i-2].count(1)>4<l[i+2].count(1)
p=lambda g,e=enumerate:[[w%2or[8,6][f(g,i)|f([*zip(*g)],j)]for j,w in e(v)]for i,v in e(g)]