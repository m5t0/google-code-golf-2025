def p(g):
 for _ in' '*4:u=[r for r in g if r.count(max([*filter(any,g)][0]))-1];g=[*zip(*(len(g)-len(u))*g[:1]+u)][::-1]
 return g