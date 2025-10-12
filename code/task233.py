def p(u):
 c={};o=lambda a:[a(p,s,[u[p+a//3][s+a%3]for a in range(9)])for p in range(len(u)-2)for s in range(len(u[0])-2)]
 def p(p,s,e):
  if len(r:={*e})==2and r&{0,2}=={2}:
   e=(*(a==2for a in e),);k={e:sum(r)-2}
   for a in range(9):u[p+a//3][s+a%3]=0
   for a in range(4):c[e]=k;e=(*(e[a%3*3+2-a//3]for a in range(9)),)
 o(p);*u,=map(list,zip(*filter(any,zip(*filter(any,u)))));[o(lambda p,s,e:(t:=c.get(e:=(*(a==0for a in e),)))and(a or e in t)and(r:=t.popitem()[1],[u[p+a//3].__setitem__(s+a%3,(r,2)[e[a]])for a in range(9)]))for a in range(2)];return u