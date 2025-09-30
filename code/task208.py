def p(g):
 v=sum(g,[]);w=g[v.index(M:=min(v,key=v.count))//21].count(M)-2;h=v.count(M)//2-w-2
 for i in range((21-h)*(21-w)):
  L,K=divmod(i,21-h)
  for V in(any(any(v[L:L+w])for v in g[K:K+h])<1)*g[K-1:K+h+1]:V[L-1:L+w+1]=[M]+[any(V[L:L+w])*M]*w+[M]
 return g