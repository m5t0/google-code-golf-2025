def p(o):
 n=13;r={f:[(i//n,i%n)for i in range(169)if o[i//n][i%n]==f]for f in range(169)};t={f:((p,n),[(d,i-p,(e-n)*[-1,1][f-2])for i,e in r[d]])for f in(2,3)for d in range(169)for p,n in r[f]if{(p+d//3-1,n+d%3-1)for d in range(9)if d-4}&{*r[d]}}
 for f in t:
  for p,n in r[f]:
   for d,i,e in t[f][1]*((p,n)!=t[f][0]):o[i+p][e+n]=d
 return o