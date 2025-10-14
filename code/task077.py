def p(e,p=range):
 for t in p(24):
  for t in p(len(e)-1):
   for a in p(len(e[0])-1):
    if(e[t+1][a]in[2,4])*(e[t][a]-2)*(e[t][a+1]in[2,4]or t*(e[t-1][a]==2)):e[t][a]=4
  *e,=map(list,zip(*e[::-1]))
 return e