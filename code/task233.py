def p(a):
 l={};n=lambda m:[m(p,h,[a[p+m//3][h+m%3]for m in range(9)])for p in range(len(a)-2)for h in range(len(a[0])-2)]
 def p(p,h,n):
  if len(r:={*n})==2and r&{0,2}=={2}:
   n=(*(m==2for m in n),);t={n:sum(r)-2}
   for m in range(9):a[p+m//3][h+m%3]=0
   for m in range(4):l[n]=t;n=(*(n[m%3*3+2-m//3]for m in range(9)),)
 n(p);*a,=map(list,zip(*filter(any,zip(*filter(any,a)))));[n(lambda p,h,n:(r:=l.get(n:=(*(m==0for m in n),)))and(m or n in r)and(r:=r.popitem()[1],[a[p+m//3].__setitem__(h+m%3,(r,2)[n[m]])for m in range(9)]))for m in range(2)];return a