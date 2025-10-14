d=range(10)
s=lambda n:{n-1:d[:n],n:[n],n+1:[n+1],n+2:d[n+2:]}
p=lambda n:[[m in(i:=s((u:=sum(n,[]).index(2))//10))and a in(e:=s(u%10))and max(n[u][m]for u in i[m]for m in e[a])for a in d]for m in d]