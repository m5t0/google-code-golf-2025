def p(g):
 a=[s:=[3]*4+[0]*5]*4+[[0]*4+s[:5]]*4+[[0]*9]
 for k in g[0][0],g[0][2],g[2][2],g[2][0]:
  if k:break
  *a,=zip(*a[::-1])
 return a