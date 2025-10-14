def p(p):
 r=13;o={i:[(t//r,t%r)for t in range(169)if p[t//r][t%r]==i]for i in range(169)};d={i:((n,r),[(f,t-n,(e-r)*[-1,1][i-2])for t,e in o[f]])for i in(2,3)for f in range(169)for n,r in o[i]if{(n+f//3-1,r+f%3-1)for f in range(9)if f-4}&{*o[f]}}
 for i in d:
  for n,r in o[i]:
   for f,t,e in d[i][1]*((n,r)!=d[i][0]):p[t+n][e+r]=f
 return p