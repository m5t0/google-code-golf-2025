def p(g):
 d=0,1,0,-1;c=eval(str(g))
 for I in range((b:=len(g))*b*4):
  if g[i:=I//4//b][j:=I//4%b]*(b>i+(z:=d[k:=I%4])>-1<i+(x:=d[a:=-~k&3])<b>j+x>-1<j+(y:=d[-~a&3])<b and g[i+z][j+x]<1>g[i+x][j+y]):
   e=v=1
   while(s:=j+e*(x+y))>-1<(t:=i+e*(z+x))<b>s:
    if v>1:c[t][s]=c[i][j]
    v+=g[t][s];e+=1
 return c