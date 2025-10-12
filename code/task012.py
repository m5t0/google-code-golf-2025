def p(r,e=range(-2,10)):
 for p in e:
  for o in e:
   for a in((n:=r[p+1][o])==r[p-1][o]==r[p][o+1]>0)*[*e[:5]]:d=r[p][o];r[p-a][o]=r[p][o-a]=n;r[p+a][o+a]=r[p+a][o-a]=d
 return r