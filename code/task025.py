def p(g):
 l=len;g=[z:=[*zip(*g)],g][v:=any(l({*c})<2for c in z)];n=l(g[0]);o=[n*[0]for _ in[0]*l(g)]
 for s in range(l(g)*n):
  if(c:=(b:=g[i:=s//n])[j:=s%n])*(l({*[*zip(*g)][j]})<2):
   a=o[i];a[j]=c;a[j-1]=c*(c in b[:j])
   if j<n-1:a[j+1]=c*(c in b[j+1:])
 return([*map(list,zip(*o))],o)[v]