def p(g):
 def f(c,s):
  a,b=[(i,v.index(c))for i,v in enumerate(g)if c in v][0]
  while g[a:a+1]and g[a][b:b+1]:g[a][b]=c;a+=s;b+=s
 f(1,-1);f(2,1);return g