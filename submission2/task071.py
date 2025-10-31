def p(o):
	B=sum(o,[]);A,E=sorted(map(B.index,{*B}-{0}));C=E&15;A=A%16+15-B[A|15::-1].index(B[A])
	for D in o:D[C:C+4]=D[A-C:A-C-4:-1]
	return o