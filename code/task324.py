def p(q,t=range):
 s,l,n,a,o=[],len(q[0]),len(q),[q]*5,sum(q,[])
 for m in t(9):s+=[m+1]*(0<o.count(m+1)<3)
 i=d=q[0][q[0][0]in s];o=sum({*o}-{*s,i})
 if any(q[m][n]==s[0]and sum((m==i)-(m==o)for v in q[m and m-1:m+2]for m in v[n and n-1:n+2])>0for m in t(n)for n in t(l)):d=o
 for m in t(4):
  a=[[*map(list,zip(*n))][::-1]for n in a];v=a[m]
  for m in t(len(v)-1):
   for p in t(len(v[0])-1):
    if v[m][p]in s:v[m+1][p+1]=a[4][m+1][p+1]=s[0]
 return[[[a[4][n][p],s[q[n][p]in(d,s[1])]][a[4][n][p]in s]for p in t(l)]for n in t(n)]