f=lambda v,c:v[:[*v,c].index(c)]
p=lambda g,e=enumerate:max((str(s:=[f(g[i+I][j:])for I,_ in e(f(w[i:]))]).count(str(min(v:=sum(g,[]),key=v.count))),-i-j,s)for j,w in e(zip(*g))for i,_ in e(g))[2]