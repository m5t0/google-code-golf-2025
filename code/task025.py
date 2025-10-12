def p(g):
 e=len;*o,=zip(*g);g=[o,g][v:=1in{e({*f})for f in o}];n=e(g[0]);o=[n*[0]for _ in g]
 for s in range(e(g)*n):
  if(f:=(l:=g[r:=s//n])[h:=s%n])*(e({*[*zip(*g)][h]})<2):
   i=o[r];i[h]=f;i[h-1]=f*(f in l[:h])
   if h<n-1:i[h+1]=f*(f in l[h+1:])
 return([*zip(*o)],o)[v]