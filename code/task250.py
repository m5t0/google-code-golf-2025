r=range(10)
s=lambda m:{m-1:r[:m],m:[m],m+1:[m+1],m+2:r[m+2:]}
p=lambda n:[[i in(b:=s((a:=sum(n,[]).index(2))//10))and m in(p:=s(a%10))and max(n[a][i]for a in b[i]for i in p[m])for m in r]for i in r]