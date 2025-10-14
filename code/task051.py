def p(t):
	o=len(t);d=len(t[0]);m=sum(t,[]);n=min({*m}-{0},key=m.count);i,e=divmod(m.index(n),d);k,u=next((m,n)for(m,n)in((0,1),(1,0),(0,-1),(-1,0))if(0<=i+m<o)*(0<=e+n<d)*t[i+m][e+n]<1)
	while(-1<(i:=i-k)<o)&(-1<(e:=e-u)<d):t[i][e]=t[i][e]or n
	return t