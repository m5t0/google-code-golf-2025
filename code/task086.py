def p(g,r=range):
 f=[*map(list,g)]
 for k in r(200):
  if g[(i:=k%100//10)+(l:=3+k//100):]and{*g[i][(j:=k%10):j+l]+g[s:=i+l-1][j:j+l]}=={h:=g[i][j]}and h:
   for d in r(l*(l*3-4)):f[i+(x:=d//l-l+2)][b:=j+(y:=d%l)]=f[a:=i+y][j+x]=h;f[i][b]=f[s][b]=f[a][j]=f[a][j+l-1]=g[i+1][j+1]
 return f