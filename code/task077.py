def p(i,p=range):
 for a in p(24):
  for a in p(len(i)-1):
   for g in p(len(i[0])-1):
    if(i[a+1][g]in[2,4])*(i[a][g]-2)*(i[a][g+1]in[2,4]or a*(i[a-1][g]==2)):i[a][g]=4
  *i,=map(list,zip(*i[::-1]))
 return i