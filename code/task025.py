def p(g):
 r,m,n,f=range,len(g),len(g[0]),lambda c,l:c*any(x==c for x in l);o=[[0]*n for i in r(m)]
 for s in r(m*n):
   if(c:=g[i:=s//n][j:=s%n]):
    if len({*(h:=[*zip(*g)][j])})<2:
      o[i][j]=c
      if j<n-1:o[i][j+1]=f(c,g[i][j+1:])
      if j>0:o[i][j-1]=f(c,g[i][:j])
    elif len({*g[i]})<2:
      o[i][j]=c
      if i<m-1:o[i+1][j]=f(c,h[i+1:])
      if i>0:o[i-1][j]=f(c,h[:i])
 return o