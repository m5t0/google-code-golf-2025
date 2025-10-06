def p(g):
 (I,J),_,_,(K,L),*a=[(i,j)for i in range(13)for j in range(13)if g[i][j]==4]
 for v in g[I:K+1]:a+=[v[J:L+1]];v[J:L+1]=[0]*(L-J+1)
 b=[[w[0]for w in zip(v,*g)if any(w)]for v in g if any(v)];return[a[0],*[[a[1][0]]+v[::1-2*(a[1][0]in[*zip(*b)][-1])]+[a[1][-1]]for v in b],a[-1]]