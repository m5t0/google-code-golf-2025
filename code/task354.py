def p(g):
 h=g[0]
 for r in g:
  j=0
  while j-10:
   if r[j]-5:j+=1;continue
   k=j
   while k-10 and r[k]==5:k+=1
   r[j:k]=[max(h[j:k])]*(k-j);j=k
 return g