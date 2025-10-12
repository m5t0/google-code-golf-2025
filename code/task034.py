r=range(9)
f=lambda p:min(i for i in r if any(p[i]))
p=lambda o:[[max((m:=o[(p:=f(o))+e//2][(a:=f([*zip(*o)]))+e%2])*(m!=2)for e in r[:4])*max((o[m:=p+e//2][n:=a+e%2]==2)*(2>((m:=(i-m)//(e//2*2-1))-(k-n)//(e%2*2-1))>=-1<m)for e in r[:4])or o[i][k]for k in r]for i in r]