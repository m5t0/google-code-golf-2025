# 1 fail、それさえ何とかしたら最短な気がする
p=lambda g,r=range(30):min([t for c in r if(t:=[[v[j]for j in r if c in[*zip(*g)][j]]for v in g if c in v])],key=len)