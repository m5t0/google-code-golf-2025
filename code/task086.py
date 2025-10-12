def p(r):
 f=eval(str(r))
 for y in range(200):
  for y in range(r[(l:=y//100+3)+(p:=y//10%10):]>[]and{*r[p][(n:=y%10):n+l]+r[s:=p+~-l][n:n+l]}=={z:=r[p][n]}!={0}and l*l*3-4*l):f[p+(u:=y//l-l+2)][e:=n+(a:=y%l)]=f[a:=p+a][n+u]=z;f[p][e]=f[s][e]=f[a][n]=f[a][n+~-l]=r[p+1][n+1]
 return f