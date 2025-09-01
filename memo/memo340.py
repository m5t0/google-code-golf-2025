# これを短縮した方が良い可能性はあり。
f=lambda v,j,m:v[0]*(j==1)*(v[0]in v[1:])+v[-1]*(j==m-2)*(v[-1]in v[:-1])
p=lambda g,e=enumerate:[[[f(v,j,m:=len(g[0]))+f(w,i,n:=len(g)),v[j]][min(i,n-1-i,j,m-1-j)<1]for j,w in e(zip(*g))]for i,v in e(g)]