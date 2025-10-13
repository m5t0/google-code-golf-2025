def p(q,r=range):
 s,l,n,e,o=[],len(q[0]),len(q),[q]*5,sum(q,[])
 for i in r(9):s+=[i+1]*(0<o.count(i+1)<3)
 a=d=q[0][q[0][0]in s];o=sum({*o}-{*s,a})
 if any(q[i][n]==s[0]and sum((i==a)-(i==o)for v in q[i and i-1:i+2]for i in v[n and n-1:n+2])>0for i in r(n)for n in r(l)):d=o
 for i in r(4):
  e=[[*map(list,zip(*n))][::-1]for n in e];v=e[i]
  for i in r(len(v)-1):
   for u in r(len(v[0])-1):
    if v[i][u]in s:v[i+1][u+1]=e[4][i+1][u+1]=s[0]
 return[[[e[4][n][u],s[q[n][u]in(d,s[1])]][e[4][n][u]in s]for u in r(l)]for n in r(n)]