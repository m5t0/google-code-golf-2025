r=range(9)
f=lambda x:min(i for i in r if any(x[i]))
p=lambda n:[[max((p:=n[(x:=f(n))+k//2][(y:=f([*zip(*n)]))+k%2])*(p!=2)for k in r[:4])*max((n[q:=x+k//2][p:=y+k%2]==2)*(2>((q:=(i-q)//(k//2*2-1))-(a-p)//(k%2*2-1))>=-1<q)for k in r[:4])or n[i][a]for a in r]for i in r]