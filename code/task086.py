def p(o):
 f=eval(str(o))
 for a in range(200):
  for a in range(o[(r:=a//100+3)+(e:=a//10%10):]>[]and{*o[e][(u:=a%10):u+r]+o[p:=e+~-r][u:u+r]}=={l:=o[e][u]}!={0}and r*r*3-4*r):f[e+(d:=a//r-r+2)][t:=u+(a:=a%r)]=f[a:=e+a][u+d]=l;f[e][t]=f[p][t]=f[a][u]=f[a][u+~-r]=o[e+1][u+1]
 return f