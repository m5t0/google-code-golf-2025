r=range(9)
f=lambda x:min(i for i in r if any(x[i]))
p=lambda g:[[max((v:=g[(x:=f(g))+k//2][(y:=f([*zip(*g)]))+k%2])*(v!=2)for k in r[:4])*max((g[t:=x+k//2][u:=y+k%2]==2)*(2>((w:=(i-t)//(k//2*2-1))-(j-u)//(k%2*2-1))>=-1<w)for k in r[:4])or g[i][j]for j in r]for i in r]