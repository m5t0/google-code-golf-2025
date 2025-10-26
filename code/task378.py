def p(g,t=7):
 for q in(v:=sum(g,[])):
  I,J=divmod(v.index(q),s:=len(g));k=0
  while J>k<I<s-2>J>0<q!=(o:=g[I+2][J+2])>0:k+=1;g[I-k][J-k]=o
 return-t*g or p([*map(list,zip(*g))][::-1],t-1)