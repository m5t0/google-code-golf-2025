def p(g):
 d={8:4,2:1,3:6}
 E=enumerate
 X=[[C for i,C in E(R)] for R in g]
 for r,R in E(g):
  for c,C in E(R):
   if C>0:
    for i in range(-1,2):
     for j in range(-1,2):
      try:
       if [i,j]!=[0,0]:X[r+i][c+j]=d[C]
      except:pass
 return X
