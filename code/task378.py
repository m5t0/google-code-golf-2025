def p(g,r=range):
 d=0,1,0,-1;c=eval(str(g))
 for I in r((b:=len(g))*b*4):
  if g[i:=I//4//b][j:=I//4%b]*(b>i+d[k:=I%4]>-1<i+d[a:=-~k&3]<b>j+d[a]>-1<j+d[u:=-~a&3]<b and g[i+d[k]][j+d[a]]<1>g[i+d[a]][j+d[u]]):
   e=v=1
   while(s:=j+e*(d[a]+d[u]))>-1<(t:=i+e*(d[k]+d[a]))<b>s:
    if v>1:c[t][s]=c[i][j]
    v+=g[t][s];e+=1
 return c