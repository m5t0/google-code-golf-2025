def p(g,s=0):
 for v in g:
  if 4in v:i=v.index;a=i(4);b=i(4,a+1);s^=1
  elif s:v[a+1:b]=[2]*(b+~a)
 return g