def p(g):
 a=sum(g,[]);b=a.index(1);c=528-a[::-1].index(1);m=c//23-b//23+1;f=n=c%23-b%23+1;h=range(m*n)
 for _ in range(8):
  for i in range(-9,24):
   for l in range(-9,24):
    for j,k in[*zip(range(m*n),h)]*all((23>i+k//n>-1<l+k%n<23)<1>=g[b//23+j//f][b%23+j%f]or(23>i+k//n>-1<l+k%n<23and(g[b//23+j//f][b%23+j%f]<3>g[i+k//n][l+k%n]or g[b//23+j//f][b%23+j%f]==g[i+k//n][l+k%n]))for j,k in zip(range(m*n),h)):
     if 23>i+k//n>-1<l+k%n<23:g[i+k//n][l+k%n]=g[b//23+j//f][b%23+j%f]
  h=[[n-1-i%n,i%n][_%4>2]*m+i//n for i in h];m,n=n,m
 return g