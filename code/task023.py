def p(g):
 for i,r in enumerate(g):
  if 5in r:j=r.index(5);break
 else:return 1
 if[5]==r[j+1:j+2]and(h:=g[i+1])[j:j+2]==[5,5]:
  r[j:j+2]=h[j:j+2]=8,8
  if p(g):return g
  r[j:j+2]=h[j:j+2]=5,5
 if r[j+1:j+3]==[5,5]:
  r[j:j+3]=[2]*3
  if p(g):return g
  r[j:j+3]=[5]*3
 if[*zip(*g)][j][i+1:i+3]==(5,5):
  r[j]=g[i+1][j]=g[i+2][j]=2
  if p(g):return g
  r[j]=g[i+1][j]=g[i+2][j]=5