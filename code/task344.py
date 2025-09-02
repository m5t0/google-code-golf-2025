def p(g,r=range):
 h,w=len(g),len(g[0]);d=0,1,0,-1
 for K in r(h*w*4):
  if h>(a:=(i:=K//4//w)+d[J:=K%4])>-1<(b:=(j:=K//4%w)+d[J-1])<w and g[a][b]==g[i][j]-1:g[i][j]=8;g[a][b]=0
 return g