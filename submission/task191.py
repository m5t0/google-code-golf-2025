def p(x):
 u=sum(x,[]);p=528-u[::-1].index(1);e=u.index(1);N=23;r=(p-e)//N+1;d=n=p%N-e%N+1;l=range(r*n);R=range(-9,24)
 for o in range(8):
  for i in R:
   for a in R:
    for u,f in[*enumerate(l)]*all((N>i+f//n>-1<a+f%n<N)<1>=x[e//N+u//d][e%N+u%d]or(N>i+f//n>-1<a+f%n<N and(x[e//N+u//d][e%N+u%d]<3>x[i+f//n][a+f%n]or x[e//N+u//d][e%N+u%d]==x[i+f//n][a+f%n]))for u,f in enumerate(l)):
     if N>i+f//n>-1<a+f%n<N:x[i+f//n][a+f%n]=x[e//N+u//d][e%N+u%d]
  l=[[n-1-i%n,i%n][o&3>2]*r+i//n for i in l];r,n=n,r
 return x
