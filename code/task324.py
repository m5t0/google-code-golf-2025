def p(g,r=range):
 c,m,n,l,t=[],len(g[0]),len(g),[g]*5,sum(g,[])
 for i in r(9):c+=[i+1]*(0<t.count(i+1)<3)
 a=d=g[0][g[0][0]in c];z=sum({*t}-{*c,a})
 if any(g[i][j]==c[0]and sum((x==a)-(x==z)for v in g[i and i-1:i+2]for x in v[j and j-1:j+2])>0for i in r(n)for j in r(m)):d=z
 for i in r(4):
  l=[[*map(list,zip(*j))][::-1]for j in l];v=l[i]
  for x in r(len(v)-1):
   for y in r(len(v[0])-1):
    if v[x][y]in c:v[x+1][y+1]=l[4][x+1][y+1]=c[0]
 return[[[l[4][j][k],c[g[j][k]in(d,c[1])]][l[4][j][k]in c]for k in r(m)]for j in r(n)]