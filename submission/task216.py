f=lambda v:v[:v.index(0)]if 0in v else v
p=lambda g,e=enumerate:min([[f(g[i+I][j:])for I,_ in e(f(w[i:]))]for j,w in e(zip(*g))for i,v in e(g)],key=lambda g:-str(g).count("2"))