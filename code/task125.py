def p(r):
	C=[8]*17;r=[C]+[[8]+A+[8]for A in r]+[C];D=-1,0,1
	for E in(4,5):
		for F in range(225):A=F//15+1;B=F%15+1;G=[r[A+C][B+E]for C in D for E in D];r[A][B]-=E*(r[A][B]>7 and[sum(G)<66,6 in G][E&1])
	return[A[1:-1]for A in r[1:-1]]