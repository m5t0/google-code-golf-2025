def p(j):
	A=6*(j[3][3]<1)
	for B in range(3):j[B][A:A+3]=j[B][3:6][::-1]
	return j