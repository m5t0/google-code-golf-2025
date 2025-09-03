def p(g,r=range(14)):
 if any([v==5for v in g[0]]):return[*map(list,zip(*p([*zip(*g)])))]
 a,b=min(s:=[i for i in r if 5in g[i]]),max(s);return[[(a-sum(v>0for v in x[:a])<=i<=b+sum(v>0for v in x[b+1:]))*5for x in zip(*g)]for i in r]