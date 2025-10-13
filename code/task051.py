def p(a):
	F=len(a);C=len(a[0]);D=sum(a,[]);E=min({*D}-{0},key=D.count);A,B=divmod(D.index(E),C);G,H=next((D,E)for(D,E)in((0,1),(1,0),(0,-1),(-1,0))if(0<=A+D<F)*(0<=B+E<C)*a[A+D][B+E]<1)
	while(-1<(A:=A-G)<F)&(-1<(B:=B-H)<C):a[A][B]=a[A][B]or E
	return a