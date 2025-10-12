def p(g):
 m=len(g[0]);R=~-m//5*2+1;h=[R*[M:=max(v:=sum(g,[]),key=v.count)]for _ in[R]*R]
 for k in{*v}-{M}:
  a=[divmod(i,m)for i,x in enumerate(v)if x==k];i,j=a[0];I,J=a[3]
  for X,Y in a:h[X+(R-I-i)//2][Y+(R-J-j)//2]=k
 return h