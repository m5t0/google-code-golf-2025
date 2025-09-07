def p(g):
 l=len;g=[z:=[*zip(*g)],g][v:=1in{l({*c})for c in z}];n=l(g[0]);o=[n*[0]for _ in g]
 for s in range(l(g)*n):
  if(c:=(b:=g[i:=s//n])[j:=s%n])*(l({*[*zip(*g)][j]})<2):
   a=o[i];a[j]=c;a[j-1]=c*(c in b[:j])
   if j<n-1:a[j+1]=c*(c in b[j+1:])
 return([*zip(*o)],o)[v]