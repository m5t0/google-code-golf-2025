def p(x):
 u=sum(x,[]);p=528-u[::-1].index(1);e=u.index(1);r=p//23-e//23+1;d=n=p%23-e%23+1;l=range(r*n)
 for o in range(8):
  for i in range(-9,24):
   for a in range(-9,24):
    for u,f in[*zip(range(r*n),l)]*all((23>i+f//n>-1<a+f%n<23)<1>=x[e//23+u//d][e%23+u%d]or(23>i+f//n>-1<a+f%n<23and(x[e//23+u//d][e%23+u%d]<3>x[i+f//n][a+f%n]or x[e//23+u//d][e%23+u%d]==x[i+f//n][a+f%n]))for u,f in zip(range(r*n),l)):
     if 23>i+f//n>-1<a+f%n<23:x[i+f//n][a+f%n]=x[e//23+u//d][e%23+u%d]
  l=[[n-1-i%n,i%n][o%4>2]*r+i//n for i in l];r,n=n,r
 return x