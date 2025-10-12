def p(f):
 for s,e in enumerate(f):
  if 5in e:n=e.index(5);break
 else:return 1
 if[5]==e[n+1:n+2]and f[s+1][n:n+2]==[5,5]:
  e[n:n+2]=f[s+1][n:n+2]=8,8
  if p(f):return f
  e[n:n+2]=f[s+1][n:n+2]=5,5
 if e[n+1:n+3]==[5,5]:
  e[n:n+3]=2,2,2
  if p(f):return f
  e[n:n+3]=5,5,5
 if s<6and f[s+1][n]==f[s+2][n]==5:
  e[n]=f[s+1][n]=f[s+2][n]=2
  if p(f):return f
  e[n]=f[s+1][n]=f[s+2][n]=5