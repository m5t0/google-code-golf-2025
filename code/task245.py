f=lambda g,k:[k in v for v in g].index(1)
p=lambda g,k=1:-k*g or p([[x//3*3|(w[i+f(g,2)+~f(g,3)]==2)*2for i,x in enumerate(w)]for w in zip(*g)],k-1)