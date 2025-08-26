def p(g):
 o=[[0]*3for _ in[0,1,2]]
 for s in range(729):
  if(g[i:=1+s//81][j:=1+s//9%9]==5)*(v:=g[i+s%9//3-1][j+s%3-1]):o[s%9//3][s%3]=v
 return o