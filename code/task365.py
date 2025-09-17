def p(g):
 A=B=C=D=E=0
 for k in range(99):
  c=d=0;i,j=k//10,k%10
  while i+c<10and g[i+c][j]:c+=1
  while j+d<10and g[i][j+d]:d+=1
  if(f:=sum(t[j:j+d].count(2)for t in g[i:i+c]))>E:A,B,C,D,E=i,j,c,d,f
 return[r[B:B+D]for r in g[A:A+C]]