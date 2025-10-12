def p(x):
 for r,e in enumerate(x):
  if 5in e:f=e.index(5);break
 else:return 1
 if[5]==e[f+1:f+2]and x[r+1][f:f+2]==[5,5]:
  e[f:f+2]=x[r+1][f:f+2]=8,8
  if p(x):return x
  e[f:f+2]=x[r+1][f:f+2]=5,5
 if e[f+1:f+3]==[5,5]:
  e[f:f+3]=2,2,2
  if p(x):return x
  e[f:f+3]=5,5,5
 if r<6and x[r+1][f]==x[r+2][f]==5:
  e[f]=x[r+1][f]=x[r+2][f]=2
  if p(x):return x
  e[f]=x[r+1][f]=x[r+2][f]=5