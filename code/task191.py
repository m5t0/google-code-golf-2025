def p(g):
 s=sum(g,[]);c=528-s[::-1].index(1);b=s.index(1);r=c//23-b//23+1;d=n=c%23-b%23+1;h=range(r*n)
 for _ in range(8):
  for i in range(-9,24):
   for l in range(-9,24):
    for s,k in[*zip(range(r*n),h)]*all((23>i+k//n>-1<l+k%n<23)<1>=g[b//23+s//d][b%23+s%d]or(23>i+k//n>-1<l+k%n<23and(g[b//23+s//d][b%23+s%d]<3>g[i+k//n][l+k%n]or g[b//23+s//d][b%23+s%d]==g[i+k//n][l+k%n]))for s,k in zip(range(r*n),h)):
     if 23>i+k//n>-1<l+k%n<23:g[i+k//n][l+k%n]=g[b//23+s//d][b%23+s%d]
  h=[[n-1-i%n,i%n][_%4>2]*r+i//n for i in h];r,n=n,r
 return g