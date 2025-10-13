def p(r):
 f=[[(d//13,d%13)for d in range(169)if r[d//13][d%13]==e]for e in range(169)];u={e:((p,a),[(i,d-p,(t-a)*(2*e-5))for d,t in f[i]])for e in(2,3)for i in range(169)for p,a in f[e]if{(p+i//3-1,a+i%3-1)for i in range(9)if i-4}&{*f[i]}}
 for e in u:
  for p,a in f[e]:
   for i,d,t in u[e][1]*((p,a)!=u[e][0]):r[d+p][t+a]=i
 return r