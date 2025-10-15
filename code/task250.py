m=range(10)
e=lambda d:{d-1:m[:d],d:[d],d+1:[d+1],d+2:m[d+2:]}
p=lambda d:[[a in(x:=e((n:=sum(d,[]).index(2))//10))and m in(g:=e(n%10))and max(d[n][a]for n in x[a]for a in g[m])for m in m]for a in m]