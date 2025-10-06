def p(g):
 v=sum(g,[]);e=max(v,key=v.count);l=sorted({*v}-{e})
 for c in l:
  a=[[[e,x][x==c]for*w,x in zip(*g,v)if c in w]for v in g if c in v];d=[[w for w in r for _ in'00']for r in a for _ in'00']
  for h in l:
   for i in range(1-len(d),(N:=len(g))):
    for j in range(1-(M:=len(d[0])),(O:=len(g[0]))):
     if all(s:=[[e,u:=g[i+x][j+y]][u==h]*((u==h)==(d[x][y]==c))for x in range(len(d))for y in range(M)if N>i+x>-1<j+y<O])>0<s.count(h)==v.count(h):return a