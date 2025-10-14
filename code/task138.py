def p(i,p=enumerate):
 for a in[0]*4:i=[*zip(*[n for a,n in p(i)if any(map(all,i[:a+1]))])][::-1]
 for a in[0]*4:i=[*zip(*[[e or n[0]*(n[0]in n[a:])for a,e in p(n)]for n in i])][::-1]
 return i