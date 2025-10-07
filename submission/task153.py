def p(g):
 m=max({*(v:=sum(g,[]))}-{0},key=v.count)
 return[[w[0]or(sum({*sum(g,[])})-m)for w in zip(v,*g)if m in w]for v in g if m in v]