def p(m,e=enumerate):
 def f(u,c,p,q,i):
  u+=p;c+=q;a=0
  if i>2or not(m[u:u+1]and(e:=m[u])[c:c+1])or(a:=e[c]):return a>5or a==2and 2
  e[c]=3;a=f(u,c,p,q,i)
  if a>1or a and(f(u,c,-q,-p,i+1)>1or f(u,c,q,p,i+1)>1):return 2
  e[c]=0;return 0
 for(u,c),(n,a)in(e:=[(u,c)for u,a in e(m)for c,a in e(a)if a==3]),e[::-1]:
  if f(u,c,u-n,c-a,0)>1:return m