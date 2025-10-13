def p(w):
 for x,e in enumerate(w):
  if 5in e:r=e.index(5);break
 else:return 1
 if[5]==e[r+1:r+2]and w[x+1][r:r+2]==[5,5]:
  e[r:r+2]=w[x+1][r:r+2]=8,8
  if p(w):return w
  e[r:r+2]=w[x+1][r:r+2]=5,5
 if e[r+1:r+3]==[5,5]:
  e[r:r+3]=2,2,2
  if p(w):return w
  e[r:r+3]=5,5,5
 if x<6and w[x+1][r]==w[x+2][r]==5:
  e[r]=w[x+1][r]=w[x+2][r]=2
  if p(w):return w
  e[r]=w[x+1][r]=w[x+2][r]=5