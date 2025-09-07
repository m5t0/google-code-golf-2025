s=0,1,2
p=lambda g:[[max((sum(v:=[a[3*j:3*j+3]for a in g[3*i:3*i+3]],[]).count(w:=v[k//3][k%3]),w)for k in range(9))[1]for j in s]for i in s]