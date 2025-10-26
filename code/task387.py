def p(o):
 (r,t),*e,(s,f)=i=[(s,h)for s,f in enumerate(o)for h,d in enumerate(f)if d]
 for u,(s,h)in enumerate(i):
  for m in-1,0,1:
   for d in-1,0,1:
    if m|d:o[s+m][h+d]=o[r][[f,t][0<u<3]]
 for n in range(2,(s-r)//2+1,2):
  for m in t,f:o[r+n][m]=o[s-n][m]=5
 for n in range(2,(f-t)//2+1,2):
  for m in r,s:o[m][t+n]=o[m][f-n]=5
 return o