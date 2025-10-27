def p(g):
 for c in 1,2:
  a,b=divmod(sum(g,[]).index(c),10);s=2*c-3
  while-1<a<10>b>-1:g[a][b]=c;a+=s;b+=s
 return g