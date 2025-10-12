def p(o):
 n=13;r={t:[(i//n,i%n)for i in range(169)if o[i//n][i%n]==t]for t in range(169)};f={t:((p,n),[(d,i-p,(e-n)*[-1,1][t-2])for i,e in r[d]])for t in(2,3)for d in range(169)for p,n in r[t]if{(p+d//3-1,n+d%3-1)for d in range(9)if d-4}&{*r[d]}}
 for t in f:
  for p,n in r[t]:
   for d,i,e in f[t][1]*((p,n)!=f[t][0]):o[i+p][e+n]=d
 return o