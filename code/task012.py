def p(r,i=range(-2,10)):
 for n in i:
  for f in i:
   for a in((u:=r[n+1][f])==r[n-1][f]==r[n][f+1]>0)*[*i[:5]]:g=r[n][f];r[n-a][f]=r[n][f-a]=u;r[n+a][f+a]=r[n+a][f-a]=g
 return r