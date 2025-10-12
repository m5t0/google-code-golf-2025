m=range(9)
f=lambda r:min(i for i in m if any(r[i]))
p=lambda l:[[max((p:=l[(r:=f(l))+e//2][(j:=f([*zip(*l)]))+e%2])*(p!=2)for e in m[:4])*max((l[o:=r+e//2][p:=j+e%2]==2)*(2>((o:=(i-o)//(e//2*2-1))-(a-p)//(e%2*2-1))>=-1<o)for e in m[:4])or l[i][a]for a in m]for i in m]