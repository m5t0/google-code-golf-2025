d=range(10)
s=lambda r:{r-1:d[:r],r:[r],r+1:[r+1],r+2:d[r+2:]}
p=lambda r:[[o in(i:=s((l:=sum(r,[]).index(2))//10))and a in(e:=s(l%10))and max(r[l][o]for l in i[o]for o in e[a])for a in d]for o in d]