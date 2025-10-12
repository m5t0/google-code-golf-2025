def p(g):
 s=a=b=0
 for R in g:
  if 4in R:a=R.index(4);b=R.index(4,a+1);s^=1
  elif s:R[a+1:b]=[2]*(b+~a)
 return g