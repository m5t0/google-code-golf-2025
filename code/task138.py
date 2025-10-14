def p(g,e=enumerate):
 for _ in[0]*4:g=[*zip(*[v for i,v in e(g)if any(all(v)for v in g[:i+1])])][::-1]
 for _ in[0]*4:g=[*zip(*[[w or(sum({v[0]}&{*v[j:]}))for j,w in e(v)]for v in g])][::-1]
 return g