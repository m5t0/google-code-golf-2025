def p(g,r=range):
 h,w=len(g),len(g[0]);d=0,1,0,-1,0
 for i in r(h):
  for j in r(w):
   if g[i][j]==3:
    for I in r(4):
     if 0<=i+(a:=d[I])<h and 0<=j+(b:=d[I+1])<w and g[i+a][j+b]==2:g[i][j]=8;g[i+a][j+b]=0
 return g