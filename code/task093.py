def p(g,r=range(14)):
 if 5in g[0]:return[*zip(*p([*zip(*g)]))]
 a,b=min(s:=[i for i in r if 5in g[i]]),max(s);return[[(a-sum(map(bool,x[:a]))<=i<=b+sum(map(bool,x[b+1:])))*5for x in zip(*g)]for i in r]