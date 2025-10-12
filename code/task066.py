def p(r,e=enumerate):
 def p(u,j,f,q,d):
  u+=f;j+=q;a=0
  if d>2or not(r[u:u+1]and(e:=r[u])[j:j+1])or(a:=e[j]):return a>5or a==2and 2
  e[j]=3;a=p(u,j,f,q,d)
  if a>1or a and(p(u,j,-q,-f,d+1)>1or p(u,j,q,f,d+1)>1):return 2
  e[j]=0;return 0
 for(u,j),(e,a)in(e:=[(u,j)for u,a in e(r)for j,a in e(a)if a==3]),e[::-1]:
  if p(u,j,u-e,j-a,0)>1:return r