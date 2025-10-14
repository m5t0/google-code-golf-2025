def p(p):
	d=len(p);o=len(p[0]);f=sum(p,[]);l=min({*f}-{0},key=f.count);i,e=divmod(f.index(l),o);q,c=next((f,l)for(f,l)in((0,1),(1,0),(0,-1),(-1,0))if(0<=i+f<d)*(0<=e+l<o)*p[i+f][e+l]<1)
	while(-1<(i:=i-q)<d)&(-1<(e:=e-c)<o):p[i][e]=p[i][e]or l
	return p