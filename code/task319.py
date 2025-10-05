def p(g):
 v=sum(g,[]);e=max(v,key=v.count)
 f=lambda c,h,m:m(i for i,v in enumerate(h)if c in v)
 l=[([[[e,w][w==c]for w in r]for r in g],c)for c in range(10)if c in v and c-e]
 for b,c in l:
  a=[[w for w in r[f(c,zip(*b),min):f(c,zip(*b),max)+1]]for r in b[f(c,b,min):f(c,b,max)+1]]
  c=[[w for w in r for _ in'00']for r in a for _ in'00']
  for B,_ in l:
   for i in range(1-len(c),(N:=len(B))):
    for j in range(1-(M:=len(c[0])),(O:=len(B[0]))):
     s=[(u:=B[i+x][j+y])*((u!=e)==(c[x][y]!=e))for x in range(len(c))for y in range(M)if N>i+x>-1<j+y<O]
     if all(s)and s.count(t:=sum({*s}-{e}))==v.count(t)>0:return a