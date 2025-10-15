def p(p):
 n=[[(d//13,d%13)for d in range(169)if p[d//13][d%13]==e]for e in range(169)];r={e:((_,h),[(g,d-_,(t-h)*(2*e-5))for d,t in n[g]])for e in(2,3)for g in range(169)for _,h in n[e]if{(_+g//3-1,h+g%3-1)for g in range(9)if g-4}&{*n[g]}}
 for e in r:
  for _,h in n[e]:
   for g,d,t in r[e][1]*((_,h)!=r[e][0]):p[d+_][t+h]=g
 return p