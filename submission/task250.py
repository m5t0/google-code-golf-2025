r=range(10)
f=lambda I:{I-1:r[:I],I:[I],I+1:[I+1],I+2:r[I+2:]}
p=lambda g:[[i in(X:=f((x:=sum(g,[]).index(2))//10))and j in(Y:=f(x%10))and max(g[x][y]for x in X[i]for y in Y[j])for j in r]for i in r]