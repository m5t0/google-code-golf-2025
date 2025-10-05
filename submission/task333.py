f=lambda v,j:(3in v[:j])*sum(t:=v[j:])+(3in t)*sum(v[:j])
p=lambda g,e=enumerate:[[w[i]or f(v,j)+f(w,i)for j,w in e(zip(*g))]for i,v in e(g)]