def p(g):
 if c:=max((g[0]).count(k)for k in g[0])<len(g[0])*0.6:g=[*map(list,zip(*g))]
 return[x:=[[max((v.count(k),k)for k in v)[1]]*len(v)for v in g],[*map(list,zip(*x))]][c]