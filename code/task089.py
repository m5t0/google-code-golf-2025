def p(r):
 i=[[(o//13,o%13)for o in range(169)if r[o//13][o%13]==e]for e in range(169)];u={e:((g,a),[(d,o-g,(n-a)*(2*e-5))for o,n in i[d]])for e in(2,3)for d in range(169)for g,a in i[e]if{(g+d//3-1,a+d%3-1)for d in range(9)if d-4}&{*i[d]}}
 for e in u:
  for g,a in i[e]:
   for d,o,n in u[e][1]*((g,a)!=u[e][0]):r[o+g][n+a]=d
 return r