def p(g):
 i=sum(g,[]).index;m=i(1)+i(1,i(1)+1)>>1;w=len(g[0])
 for s in-w,-1,0,1,w:g[(m+s)//w][(m+s)%w]=3
 return g