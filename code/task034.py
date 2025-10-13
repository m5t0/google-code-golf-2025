y=range(9)
n=lambda f:min(i for i in y if any(f[i]))
p=lambda m:[[max((p:=m[(f:=n(m))+y//2][(a:=n([*zip(*m)]))+y%2])*(p!=2)for y in y[:4])*max((m[p:=f+y//2][g:=a+y%2]==2)*(2>((p:=(i-p)//(y//2*2-1))-(r-g)//(y%2*2-1))>=-1<p)for y in y[:4])or m[i][r]for r in y]for i in y]