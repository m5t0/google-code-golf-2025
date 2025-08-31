def p(g,r=range):
 h,w=len(g),len(g[0]);d=0,1,0,-1,0
 for I in r(h*w):
  for I in[*r(4)]*(g[i:=I//w][j:=I%w]==3):
   if h>i+(a:=d[I])>-1<j+(b:=d[I+1])<w and g[i+a][j+b]==2:g[i][j]=8;g[i+a][j+b]=0
 return g