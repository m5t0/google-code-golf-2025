f=lambda l,i:(1in l[i])*l[i-2].count(1)>4<l[i+2].count(1)
p=lambda g,e=enumerate:[[x-x//4*(f(g,i)|f([*zip(*g)],j))for j,x in e(v)]for i,v in e(g)]