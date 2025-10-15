k=lambda p,a:(len({*(n:=p[:a+1])})>1<len({*p[a:]}))*({*n}!={*p[a:]})
a=lambda p,k=min:k(p,key=p.count)
p=lambda m,o=enumerate:[[[p[o],a(p),a(n)][p[o]==a(m[0],max)and k(p,o)+k(n,b)*2]for o,n in o(zip(*m))]for b,p in o(m)]