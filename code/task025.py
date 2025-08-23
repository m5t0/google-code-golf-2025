def p(g):
 z=[*zip(*g)];v=any(len({*c})<2for c in z);g=[z,g][v];n=len(g[0]);m=len(g);o=[n*[0]for _ in[0]*m]
 for s in range(m*n):
  if(c:=g[i:=s//n][j:=s%n])and len({*[*zip(*g)][j]})<2:
   a=o[i];a[j]=c
   if j<n-1:a[j+1]=c*(c in g[i][j+1:])
   if j:a[j-1]=c*(c in g[i][:j])
 return([*map(list,zip(*o))],o)[v]