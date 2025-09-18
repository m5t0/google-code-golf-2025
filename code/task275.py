def p(g):
 n=min(len(g),len(g[0]));a,b=[v[:n]for v in g[:n]],[v[-n:]for v in g[-n:]]
 if"8"in str(a):a,b=b,a
 return[[X*x/8for x in y for X in Y]for y in a for Y in b]