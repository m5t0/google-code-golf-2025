def p(g,r=range):
 f=eval(str(g))
 for k in r(200):
  if g[(l:=k//100+3)+(i:=k//10%10):]and{*g[i][(j:=k%10):j+l]+g[s:=i+l-1][j:j+l]}=={h:=g[i][j]}and h:
   for d in r(l*(3*l-4)):f[i+(x:=d//l-l+2)][b:=j+(y:=d%l)]=f[a:=i+y][j+x]=h;f[i][b]=f[s][b]=f[a][j]=f[a][j+l-1]=g[i+1][j+1]
 return f