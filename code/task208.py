def p(g):
 v=sum(g,[]);w=g[v.index(M:=min(v,key=v.count))//(n:=len(g))].count(M)-2;h=v.count(M)//2-w-2
 for i in range((n-h)*(len(g[0])-w)):L,K=divmod(i,n-h);exec("for V in g[K-1:K+h+1]:V[L-1:L+w+1]=[M]+[({*V[L:L+w]}!={0})*M]*w+[M]"*(any(any(v[L:L+w])for v in g[K:K+h])<1))
 return g