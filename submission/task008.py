def p(g):
 for _ in' '*4:u=[v for i,v in enumerate(g)if max(v)>0 or max(max(g[:i+1]))<8];g=[*zip(*u+(len(g)-len(u))*[[0]*len(g[0])])][::-1]
 return g



def p(g):
 for _ in' '*4:u=[v for i,v in enumerate(g)if max(v)>0 or max(max(g[i:]))>7];g=[*zip(*(len(g)-len(u))*[[0]*len(g[0])]+u)][::-1]
 return g