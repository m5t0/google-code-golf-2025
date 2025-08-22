def p(g,r=range):
 o=[[0]*3for i in r(3)]
 for s in r(81):
  if g[i:=1+s//9][j:=1+s%9]==5:
   for k in r(9):
    if v:=g[i+k//3-1][j+k%3-1]:o[k//3][k%3]=v
 return o