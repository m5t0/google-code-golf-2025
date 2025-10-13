def p(g):
 b=sum(g,[]);c=528-b[::-1].index(1);r=b.index(1);a=c//23-r//23+1;d=n=c%23-r%23+1;h=range(a*n)
 for e in range(8):
  for i in range(-9,24):
   for p in range(-9,24):
    for x,b in[*zip(range(a*n),h)]*all((23>i+b//n>-1<p+b%n<23)<1>=g[r//23+x//d][r%23+x%d]or(23>i+b//n>-1<p+b%n<23and(g[r//23+x//d][r%23+x%d]<3>g[i+b//n][p+b%n]or g[r//23+x//d][r%23+x%d]==g[i+b//n][p+b%n]))for x,b in zip(range(a*n),h)):
     if 23>i+b//n>-1<p+b%n<23:g[i+b//n][p+b%n]=g[r//23+x//d][r%23+x%d]
  h=[[n-1-i%n,i%n][e%4>2]*a+i//n for i in h];a,n=n,a
 return g