def p(g):
 s=sum(g,[])
 x=max(f:=sum(g,[]),key=f.count)
 return[[w[i]for w in zip(*g)if x in w]for i in range(len(g))if x in g[i]]



def p(g):
	E=tuple(tuple(A)for A in g);U,V=len(E),len(E[0]);F=lambda x:(min(A for(A,B)in x),min(A for(B,A)in x),max(A for(A,B)in x),max(A for(B,A)in x))if x else(0,0,0,0);J=lambda x:{(A-F(x)[0],B-F(x)[1])for(A,B)in x}if x else set();G=tuple(tuple(A[::-1])for A in E);from collections import Counter as W;K=max(W(sum(G,())).items(),key=lambda kv:kv[1])[0];A={};[A.setdefault(G[B][C],set()).add((B,C))for B in range(U)for C in range(V)if G[B][C]!=K]
	C=max(A,key=lambda c:len(A[c]));H=J(A[C]);B=None
	for(L,D)in A.items():
		if L==C or len(D)==len(A[C]):continue
		X=J(D);I={(2*A+C,2*B+D)for(A,B)in X for C in(0,1)for D in(0,1)}
		if I and H:M,N,O,P=[A for(A,B)in I],[A for(B,A)in I],[A for(A,B)in H],[A for(B,A)in H];Q=max(sum((C+A,D+B)in H for(C,D)in I)for A in range(min(O)-max(M),max(O)-min(M)+1)for B in range(min(P)-max(N),max(P)-min(N)+1))
		else:Q=0
		R=Q-2*len(D),len(D),F(D)[3],L;B=R if B is None or R>B else B
	S=B[3]if B else(lambda o:max(o,key=lambda c:len(A[c]))if o else C)([A for A in A if A!=C]);Y,Z,a,b=F(A[S]);T=[list(G[A][Z:b+1])for A in range(Y,a+1)];[[A.__setitem__(B,K)for B in range(len(A))if A[B]!=S]for A in T];return[list(A[::-1])for A in T]
 
 
 
 
def p(g,r=range):
 v=sum(g,[])
 A=[divmod(v.index(x),len(g[0]))for x in{*v}-{max(v,key=v.count)}]
 a=[x for x in v if x!=M]
 m=max([x for x in{*v}-{M}],key=a.count)
 M=0
 for i,j in A:
  if g[i][j]!=m and g[i].count(g[i][j])*2==
 print([(g[i].count(g[i][j]),[*zip(*g)][j].count(g[i][j]),g[i][j])for i,j in A])