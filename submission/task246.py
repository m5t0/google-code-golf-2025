def p(g):
 (a,b),(c,d)=(divmod(sum(g,[]).index(x),len(g[0]))for x in[3,2]);g[c][b:d:b<d or-1]=[8]*abs(b-d)
 while a-c:g[a:=a+(a<c or-1)][b]=8
 return g