def p(r,o=enumerate):
 for a in[0]*4:r=[*zip(*[n for a,n in o(r)if any(map(all,r[:a+1]))])][::-1]
 for a in[0]*4:r=[*zip(*[[e or n[0]*(n[0]in n[a:])for a,e in o(n)]for n in r])][::-1]
 return r