def p(r):
 f=eval(str(r))
 for k in range(200):
  for k in range(r[(l:=k//100+3)+(i:=k//10%10):]>[]and{*r[i][(g:=k%10):g+l]+r[s:=i+~-l][g:g+l]}=={x:=r[i][g]}!={0}and l*l*3-4*l):f[i+(u:=k//l-l+2)][e:=g+(n:=k%l)]=f[a:=i+n][g+u]=x;f[i][e]=f[s][e]=f[a][g]=f[a][g+~-l]=r[i+1][g+1]
 return f