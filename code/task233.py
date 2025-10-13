def p(m):
 t={};n=lambda a:[a(p,l,[m[p+a//3][l+a%3]for a in range(9)])for p in range(len(m)-2)for l in range(len(m[0])-2)]
 def p(p,l,n):
  if len(r:={*n})==2and r&{0,2}=={2}:
   n=(*(a==2for a in n),);g={n:sum(r)-2}
   for a in range(9):m[p+a//3][l+a%3]=0
   for a in range(4):t[n]=g;n=(*(n[a%3*3+2-a//3]for a in range(9)),)
 n(p);*m,=map(list,zip(*filter(any,zip(*filter(any,m)))));[n(lambda p,l,n:(r:=t.get(n:=(*(a==0for a in n),)))and(a or n in r)and(r:=r.popitem()[1],[m[p+a//3].__setitem__(l+a%3,(r,2)[n[a]])for a in range(9)]))for a in range(2)];return m