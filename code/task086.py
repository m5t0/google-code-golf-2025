def p(g):
 f=eval(str(g))
 for k in range(200):
  for d in range(g[(l:=k//100+3)+(i:=k//10%10):]>[]and{*g[i][(j:=k%10):j+l]+g[s:=i+~-l][j:j+l]}=={h:=g[i][j]}!={0}and l*l*3-4*l):f[i+(x:=d//l-l+2)][b:=j+(y:=d%l)]=f[a:=i+y][j+x]=h;f[i][b]=f[s][b]=f[a][j]=f[a][j+~-l]=g[i+1][j+1]
 return f