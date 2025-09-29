def p(g,d=divmod):
 K,L=d(len(v:=sum(g,[]))-v[::-1].index(4)-1,13);I,J=d(v.index(4),13);a=[]
 for v in g[I:K+1]:a+=[v[J:L+1]];v[J:L+1]=[0]*(L-J+1)
 b=[[w[0]for w in zip(v,*g)if any(w)]for v in g if any(v)];return[a[0],*[[a[1][0]]+v[::1-2*(a[1][0]in[*zip(*b)][-1])]+[a[1][-1]]for v in b],a[-1]]