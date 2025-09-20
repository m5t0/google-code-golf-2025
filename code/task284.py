def p(g):
 def f(I,J,s):
  while abs((i:=A[0]+B[0]-2*I)+(j:=A[1]+B[1]-2*J))>2:g[I][J]=s;I+=(i>0)-(i<0);J+=(j>0)-(j<0)
  for k in-2,-1,1,2:g[I-i+k*j][J-j+k*i]=g[I+2*j][J+2*i]=g[I-2*j][J-2*i]=s
 v=sum(g,[]);A,B=[(*divmod(v.index(x),len(g[0])),x)for x in v if x];f(*A);f(*B);return g