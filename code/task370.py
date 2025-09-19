def p(g,r=range):
 f=lambda I,J:[k for k in r(n)if m>J+k*B>-1<I+k*A<n>g[I+k*A][J+k*B]<1]
 I=(v:=sum(g,[])).index(0);m=len(g[0]);n=len(g)
 X=v.index(M:=min(v,key=v.count))
 A,B=1-2*(X>I),1-2*(X%m>I%m)
 L=max(s:=f(X//m,X%m))-s[0]+1
 A*=L;B*=L
 return[[(s:=g[i][j])and[M,s][f(i,j)==[]]for j in r(m)]for i in r(n)]