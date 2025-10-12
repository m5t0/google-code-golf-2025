def p(g):
 u=sum(g,[]);t=528-u[::-1].index(1);e=u.index(1);r=t//23-e//23+1;d=n=t%23-e%23+1;k=range(r*n)
 for o in range(8):
  for i in range(-9,24):
   for l in range(-9,24):
    for u,f in[*zip(range(r*n),k)]*all((23>i+f//n>-1<l+f%n<23)<1>=g[e//23+u//d][e%23+u%d]or(23>i+f//n>-1<l+f%n<23and(g[e//23+u//d][e%23+u%d]<3>g[i+f//n][l+f%n]or g[e//23+u//d][e%23+u%d]==g[i+f//n][l+f%n]))for u,f in zip(range(r*n),k)):
     if 23>i+f//n>-1<l+f%n<23:g[i+f//n][l+f%n]=g[e//23+u//d][e%23+u%d]
  k=[[n-1-i%n,i%n][o%4>2]*r+i//n for i in k];r,n=n,r
 return g