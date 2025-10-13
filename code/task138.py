def p(g,e=enumerate):
 for _ in[0]*4:g=[*zip(*[v for i,v in e(g)if any(map(all,g[:i+1]))])][::-1]
 for _ in[0]*4:g=[*zip(*[[w or v[0]*(v[0]in v[j:])for j,w in e(v)]for v in g])][::-1]
 return g